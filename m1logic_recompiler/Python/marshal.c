
/* Write Python objects to files and read them back.
   This is primarily intended for writing and reading compiled Python code,
   even though dicts, lists, sets and frozensets, not commonly seen in
   code objects, are supported.
   Version 3 of this protocol properly supports circular links
   and sharing. */

#define PY_SSIZE_T_CLEAN

#include "Python.h"
#include "longintrepr.h"
#include "code.h"
#include "opcode.h"
#include "marshal.h"
#include "../Modules/hashtable.h"
#include <limits.h>

/* High water mark to determine when the marshalled object is dangerously deep
 * and risks coring the interpreter.  When the object stack gets this deep,
 * raise an exception instead of continuing.
 * On Windows debug builds, reduce this value.
 */
#if defined(MS_WINDOWS) && defined(_DEBUG)
#define MAX_MARSHAL_STACK_DEPTH 1000
#else
#define MAX_MARSHAL_STACK_DEPTH 2000
#endif

#define TYPE_NULL               '0'
#define TYPE_NONE               'N'
#define TYPE_FALSE              'F'
#define TYPE_TRUE               'T'
#define TYPE_STOPITER           'S'
#define TYPE_ELLIPSIS           '.'
#define TYPE_INT                'i'
#define TYPE_FLOAT              'f'
#define TYPE_BINARY_FLOAT       'g'
#define TYPE_COMPLEX            'x'
#define TYPE_BINARY_COMPLEX     'y'
#define TYPE_LONG               'l'
#define TYPE_STRING             's'
#define TYPE_INTERNED           't'
#define TYPE_REF                'r'
#define TYPE_TUPLE              '('
#define TYPE_LIST               '['
#define TYPE_DICT               '{'
#define TYPE_CODE               'c'
#define TYPE_UNICODE            'u'
#define TYPE_UNKNOWN            '?'
#define TYPE_SET                '<'
#define TYPE_FROZENSET          '>'
#define FLAG_REF                '\x80' /* with a type, add obj to index */

#define TYPE_ASCII              'a'
#define TYPE_ASCII_INTERNED     'A'
#define TYPE_SMALL_TUPLE        ')'
#define TYPE_SHORT_ASCII        'z'
#define TYPE_SHORT_ASCII_INTERNED 'Z'

#define WFERR_OK 0
#define WFERR_UNMARSHALLABLE 1
#define WFERR_NESTEDTOODEEP 2
#define WFERR_NOMEMORY 3

typedef struct {
    FILE *fp;
    int error;  /* see WFERR_* values */
    int depth;
    PyObject *str;
    char *ptr;
    char *end;
    char *buf;
    _Py_hashtable_t *hashtable;
    int version;
} WFILE;

#define w_byte(c, p) do {                               \
        if ((p)->ptr != (p)->end || w_reserve((p), 1))  \
            *(p)->ptr++ = (c);                          \
    } while(0)

static void
w_flush(WFILE *p)
{
    assert(p->fp != NULL);
    fwrite(p->buf, 1, p->ptr - p->buf, p->fp);
    p->ptr = p->buf;
}

static int
w_reserve(WFILE *p, Py_ssize_t needed)
{
    Py_ssize_t pos, size, delta;
    if (p->ptr == NULL)
        return 0; /* An error already occurred */
    if (p->fp != NULL) {
        w_flush(p);
        return needed <= p->end - p->ptr;
    }
    assert(p->str != NULL);
    pos = p->ptr - p->buf;
    size = PyBytes_Size(p->str);
    if (size > 16*1024*1024)
        delta = (size >> 3);            /* 12.5% overallocation */
    else
        delta = size + 1024;
    delta = Py_MAX(delta, needed);
    if (delta > PY_SSIZE_T_MAX - size) {
        p->error = WFERR_NOMEMORY;
        return 0;
    }
    size += delta;
    if (_PyBytes_Resize(&p->str, size) != 0) {
        p->ptr = p->buf = p->end = NULL;
        return 0;
    }
    else {
        p->buf = PyBytes_AS_STRING(p->str);
        p->ptr = p->buf + pos;
        p->end = p->buf + size;
        return 1;
    }
}

static void
w_string(const char *s, Py_ssize_t n, WFILE *p)
{
    Py_ssize_t m;
    if (!n || p->ptr == NULL)
        return;
    m = p->end - p->ptr;
    if (p->fp != NULL) {
        if (n <= m) {
            memcpy(p->ptr, s, n);
            p->ptr += n;
        }
        else {
            w_flush(p);
            fwrite(s, 1, n, p->fp);
        }
    }
    else {
        if (n <= m || w_reserve(p, n - m)) {
            memcpy(p->ptr, s, n);
            p->ptr += n;
        }
    }
}

static void
w_short(int x, WFILE *p)
{
    w_byte((char)( x      & 0xff), p);
    w_byte((char)((x>> 8) & 0xff), p);
}

static void
w_long(long x, WFILE *p)
{
    w_byte((char)( x      & 0xff), p);
    w_byte((char)((x>> 8) & 0xff), p);
    w_byte((char)((x>>16) & 0xff), p);
    w_byte((char)((x>>24) & 0xff), p);
}

#define SIZE32_MAX  0x7FFFFFFF

#if SIZEOF_SIZE_T > 4
# define W_SIZE(n, p)  do {                     \
        if ((n) > SIZE32_MAX) {                 \
            (p)->depth--;                       \
            (p)->error = WFERR_UNMARSHALLABLE;  \
            return;                             \
        }                                       \
        w_long((long)(n), p);                   \
    } while(0)
#else
# define W_SIZE  w_long
#endif

static void
w_pstring(const char *s, Py_ssize_t n, WFILE *p)
{
        W_SIZE(n, p);
        w_string(s, n, p);
}

static void
w_short_pstring(const char *s, Py_ssize_t n, WFILE *p)
{
    w_byte(Py_SAFE_DOWNCAST(n, Py_ssize_t, unsigned char), p);
    w_string(s, n, p);
}

/* We assume that Python ints are stored internally in base some power of
   2**15; for the sake of portability we'll always read and write them in base
   exactly 2**15. */

#define PyLong_MARSHAL_SHIFT 15
#define PyLong_MARSHAL_BASE ((short)1 << PyLong_MARSHAL_SHIFT)
#define PyLong_MARSHAL_MASK (PyLong_MARSHAL_BASE - 1)
#if PyLong_SHIFT % PyLong_MARSHAL_SHIFT != 0
#error "PyLong_SHIFT must be a multiple of PyLong_MARSHAL_SHIFT"
#endif
#define PyLong_MARSHAL_RATIO (PyLong_SHIFT / PyLong_MARSHAL_SHIFT)

#define W_TYPE(t, p) do { \
    w_byte((t) | flag, (p)); \
} while(0)

#define M1_MARKER_OPCODE 118
#define M1_MODE_DIRECT 0
#define M1_MODE_MARKER_DEFAULT 1
#define M1_MODE_MARKER_SPECIAL 2

typedef struct {
    int std_op;
    unsigned int raw_arg;
    int start_off;
    int size;
    int target_index;

    int custom_op;
    unsigned int arg1;
    unsigned int arg2;
    int mode;

    int op_pos;
    int arg_pos;
    int op_len;
    int arg_len;
} m1_instr;

static int
m1_std_to_custom(int std_op)
{
    switch (std_op) {
        case 1: return 84;
        case 2: return 46;
        case 3: return 45;
        case 4: return 34;
        case 5: return 103;
        case 11: return 44;
        case 12: return 2;
        case 15: return 24;
        case 16: return 65;
        case 17: return 109;
        case 19: return 36;
        case 20: return 43;
        case 22: return 15;
        case 23: return 32;
        case 24: return 94;
        case 25: return 51;
        case 26: return 89;
        case 27: return 86;
        case 28: return 63;
        case 29: return 93;
        case 55: return 23;
        case 56: return 20;
        case 57: return 60;
        case 59: return 38;
        case 60: return 41;
        case 61: return 17;
        case 62: return 30;
        case 63: return 88;
        case 64: return 82;
        case 65: return 61;
        case 66: return 85;
        case 67: return 9;
        case 68: return 98;
        case 69: return 59;
        case 71: return 47;
        case 72: return 3;
        case 73: return 107;
        case 75: return 96;
        case 76: return 97;
        case 77: return 28;
        case 78: return 105;
        case 79: return 80;
        case 80: return 29;
        case 81: return 53;
        case 82: return 40;
        case 83: return 19;
        case 84: return 72;
        case 86: return 4;
        case 87: return 100;
        case 88: return 18;
        case 89: return 55;
        case 90: return 239;
        case 91: return 123;
        case 92: return 210;
        case 93: return 185;
        case 94: return 206;
        case 95: return 150;
        case 96: return 161;
        case 97: return 196;
        case 98: return 159;
        case 100: return 124;
        case 101: return 199;
        case 102: return 221;
        case 103: return 125;
        case 104: return 133;
        case 105: return 245;
        case 106: return 170;
        case 107: return 253;
        case 108: return 252;
        case 109: return 248;
        case 110: return 195;
        case 111: return 140;
        case 112: return 217;
        case 113: return 151;
        case 114: return 197;
        case 115: return 240;
        case 116: return 111;
        case 119: return 110;
        case 120: return 208;
        case 121: return 220;
        case 122: return 236;
        case 124: return 127;
        case 125: return 250;
        case 126: return 112;
        case 130: return 232;
        case 131: return 149;
        case 132: return 183;
        case 133: return 184;
        case 135: return 119;
        case 136: return 167;
        case 137: return 201;
        case 138: return 222;
        case 141: return 135;
        case 142: return 238;
        case 143: return 173;
        case 144: return 118;
        case 145: return 233;
        case 146: return 188;
        case 147: return 116;
        case 148: return 224;
        case 149: return 219;
        case 150: return 215;
        case 151: return 114;
        case 152: return 113;
        case 155: return 242;
        case 156: return 249;
        case 157: return 166;
        case 158: return 169;
        default:
            return -1;
    }
}

static int
m1_is_std_jabs(int op)
{
    switch (op) {
        case JUMP_IF_FALSE_OR_POP:
        case JUMP_IF_TRUE_OR_POP:
        case JUMP_ABSOLUTE:
        case POP_JUMP_IF_FALSE:
        case POP_JUMP_IF_TRUE:
        case CONTINUE_LOOP:
            return 1;
        default:
            return 0;
    }
}

static int
m1_is_std_jrel(int op)
{
    switch (op) {
        case FOR_ITER:
        case JUMP_FORWARD:
        case SETUP_LOOP:
        case SETUP_EXCEPT:
        case SETUP_FINALLY:
        case SETUP_WITH:
            return 1;
        default:
            return 0;
    }
}

static int
m1_custom_is_dual(int op)
{
    switch (op) {
        case 110:
        case 136:
        case 140:
        case 151:
        case 173:
        case 185:
        case 195:
        case 197:
        case 208:
        case 217:
        case 220:
        case 236:
        case 240:
            return 1;
        default:
            return 0;
    }
}

static int
m1_custom_is_dual_abs(int op)
{
    switch (op) {
        case 110:
        case 140:
        case 151:
        case 197:
        case 217:
        case 240:
            return 1;
        default:
            return 0;
    }
}

static int
m1_custom_is_dual_rel(int op)
{
    switch (op) {
        case 136:
        case 173:
        case 185:
        case 195:
        case 208:
        case 220:
        case 236:
            return 1;
        default:
            return 0;
    }
}

static int
m1_parse_std_instructions(PyCodeObject *co, m1_instr **out_instrs, Py_ssize_t *out_count)
{
    const unsigned char *code_bytes;
    Py_ssize_t code_len;
    Py_ssize_t cap;
    m1_instr *ins;
    int *offset_to_index;
    Py_ssize_t i;
    Py_ssize_t count;
    unsigned int ext;
    int instr_start;

    ins = NULL;
    offset_to_index = NULL;

    if (!PyBytes_CheckExact(co->co_code)) {
        PyErr_SetString(PyExc_TypeError, "co_code is not bytes");
        return 0;
    }

    code_bytes = (const unsigned char *)PyBytes_AS_STRING(co->co_code);
    code_len = PyBytes_GET_SIZE(co->co_code);
    if ((code_len & 1) != 0) {
        PyErr_SetString(PyExc_ValueError, "co_code length must be even");
        return 0;
    }

    cap = code_len / 2;
    if (cap > 0) {
        ins = (m1_instr *)PyMem_MALLOC(sizeof(m1_instr) * cap);
        if (ins == NULL) {
            PyErr_NoMemory();
            return 0;
        }
    }

    offset_to_index = (int *)PyMem_MALLOC(sizeof(int) * (code_len + 1));
    if (offset_to_index == NULL) {
        PyMem_FREE(ins);
        PyErr_NoMemory();
        return 0;
    }
    for (i = 0; i <= code_len; i++) {
        offset_to_index[i] = -1;
    }

    count = 0;
    ext = 0;
    instr_start = -1;
    i = 0;
    while (i < code_len) {
        int op;
        int oparg;
        m1_instr *cur;

        op = code_bytes[i];
        oparg = code_bytes[i + 1];

        if (op == EXTENDED_ARG) {
            if (instr_start < 0) {
                instr_start = (int)i;
            }
            ext = (ext << 8) | (unsigned int)oparg;
            i += 2;
            continue;
        }

        cur = &ins[count];
        memset(cur, 0, sizeof(*cur));
        cur->std_op = op;
        if (op >= HAVE_ARGUMENT) {
            cur->raw_arg = ((unsigned int)oparg) | (ext << 8);
        }
        else {
            cur->raw_arg = 0;
        }
        cur->start_off = (instr_start >= 0) ? instr_start : (int)i;
        cur->size = (int)(i + 2 - cur->start_off);
        cur->target_index = -1;
        cur->mode = M1_MODE_DIRECT;

        if (cur->start_off < 0 || cur->start_off > (int)code_len) {
            PyErr_SetString(PyExc_ValueError, "invalid instruction start offset");
            goto error;
        }
        if (offset_to_index[cur->start_off] != -1) {
            PyErr_SetString(PyExc_ValueError, "duplicate instruction start offset");
            goto error;
        }
        offset_to_index[cur->start_off] = (int)count;
        count++;

        ext = 0;
        instr_start = -1;
        i += 2;
    }

    if (instr_start >= 0) {
        PyErr_SetString(PyExc_ValueError, "truncated EXTENDED_ARG chain");
        goto error;
    }

    for (i = 0; i < count; i++) {
        int target_off;

        if (m1_is_std_jabs(ins[i].std_op)) {
            if (ins[i].raw_arg > (unsigned int)INT_MAX) {
                PyErr_SetString(PyExc_ValueError, "absolute jump argument too large");
                goto error;
            }
            target_off = (int)ins[i].raw_arg;
        }
        else if (m1_is_std_jrel(ins[i].std_op)) {
            int rel;

            if (ins[i].raw_arg > (unsigned int)INT_MAX) {
                PyErr_SetString(PyExc_ValueError, "relative jump argument too large");
                goto error;
            }
            rel = (int)ins[i].raw_arg;
            if (ins[i].start_off > INT_MAX - ins[i].size - rel) {
                PyErr_SetString(PyExc_ValueError, "relative jump target overflow");
                goto error;
            }
            target_off = ins[i].start_off + ins[i].size + rel;
        }
        else {
            continue;
        }

        if (target_off < 0 || target_off > (int)code_len ||
            offset_to_index[target_off] < 0)
        {
            PyErr_SetString(PyExc_ValueError, "jump target is not a valid instruction boundary");
            goto error;
        }
        ins[i].target_index = offset_to_index[target_off];
    }

    PyMem_FREE(offset_to_index);
    *out_instrs = ins;
    *out_count = count;
    return 1;

error:
    PyMem_FREE(offset_to_index);
    PyMem_FREE(ins);
    return 0;
}

static int
m1_encode_code_bytes(PyCodeObject *co, PyObject **out_code, int *out_split)
{
    m1_instr *ins;
    Py_ssize_t ins_count;
    Py_ssize_t i;
    int iter;
    int converged;
    int op_total;
    int arg_total;
    PyObject *encoded;
    unsigned char *raw;
    unsigned char *op_stream;
    unsigned char *arg_stream;
    int op_i;
    int arg_i;

    ins = NULL;
    ins_count = 0;
    converged = 0;
    op_total = 0;
    arg_total = 0;
    encoded = NULL;
    raw = NULL;
    op_stream = NULL;
    arg_stream = NULL;
    op_i = 0;
    arg_i = 0;

    *out_code = NULL;
    *out_split = 0;

    if (!m1_parse_std_instructions(co, &ins, &ins_count)) {
        return 0;
    }

    for (i = 0; i < ins_count; i++) {
        int mapped;

        mapped = m1_std_to_custom(ins[i].std_op);
        if (mapped < 0) {
            PyErr_Format(PyExc_ValueError,
                         "unmapped opcode %d in code object",
                         ins[i].std_op);
            goto error;
        }
        ins[i].custom_op = mapped;

        if (m1_custom_is_dual(mapped)) {
            if (ins[i].target_index < 0) {
                PyErr_Format(PyExc_ValueError,
                             "dual opcode %d has no jump target",
                             mapped);
                goto error;
            }
        }
    }

    if (ins_count == 0) {
        encoded = PyBytes_FromStringAndSize("", 0);
        if (encoded == NULL) {
            goto error;
        }
        *out_code = encoded;
        *out_split = 0;
        PyMem_FREE(ins);
        return 1;
    }

    for (iter = 0; iter < 64; iter++) {
        int changed;
        int op_pos;
        int arg_pos;

        changed = 0;
        op_pos = 0;
        arg_pos = 0;

        for (i = 0; i < ins_count; i++) {
            int is_dual;

            is_dual = m1_custom_is_dual(ins[i].custom_op);
            ins[i].op_pos = op_pos;
            ins[i].arg_pos = arg_pos;

            if (ins[i].mode == M1_MODE_MARKER_DEFAULT) {
                ins[i].op_len = 2;
                ins[i].arg_len = 3;
            }
            else if (ins[i].mode == M1_MODE_MARKER_SPECIAL) {
                ins[i].op_len = 2;
                ins[i].arg_len = 4;
            }
            else {
                ins[i].op_len = 1;
                ins[i].arg_len = is_dual ? 2 : 1;
            }

            op_pos += ins[i].op_len;
            arg_pos += ins[i].arg_len;
        }

        for (i = 0; i < ins_count; i++) {
            int new_mode;
            unsigned int arg1;
            unsigned int arg2;

            new_mode = M1_MODE_DIRECT;
            arg1 = 0;
            arg2 = 0;

            if (m1_custom_is_dual(ins[i].custom_op)) {
                m1_instr *target;

                if (ins[i].target_index < 0 || ins[i].target_index >= (int)ins_count) {
                    PyErr_SetString(PyExc_ValueError, "invalid jump target index");
                    goto error;
                }
                target = &ins[ins[i].target_index];

                if (m1_custom_is_dual_abs(ins[i].custom_op)) {
                    arg1 = (unsigned int)target->op_pos;
                    arg2 = (unsigned int)target->arg_pos;
                }
                else if (m1_custom_is_dual_rel(ins[i].custom_op)) {
                    int rel_op;
                    int rel_arg;

                    rel_op = target->op_pos - (ins[i].op_pos + ins[i].op_len);
                    rel_arg = target->arg_pos - (ins[i].arg_pos + ins[i].arg_len);
                    if (rel_op < 0 || rel_arg < 0) {
                        PyErr_SetString(PyExc_ValueError,
                                        "negative relative dual jump is not supported");
                        goto error;
                    }
                    arg1 = (unsigned int)rel_op;
                    arg2 = (unsigned int)rel_arg;
                }
                else {
                    PyErr_SetString(PyExc_ValueError, "unknown dual jump type");
                    goto error;
                }

                if (arg1 <= 0xFFU && arg2 <= 0xFFU) {
                    new_mode = M1_MODE_DIRECT;
                }
                else if (arg1 <= 0xFFFFU && arg2 <= 0xFFFFU) {
                    new_mode = M1_MODE_MARKER_SPECIAL;
                }
                else {
                    PyErr_SetString(PyExc_ValueError, "dual argument exceeds 16-bit");
                    goto error;
                }
            }
            else {
                arg1 = ins[i].raw_arg;
                if (arg1 <= 0xFFU) {
                    new_mode = M1_MODE_DIRECT;
                }
                else if (arg1 <= 0xFFFFU) {
                    new_mode = M1_MODE_MARKER_DEFAULT;
                }
                else {
                    PyErr_SetString(PyExc_ValueError, "opcode argument exceeds 16-bit");
                    goto error;
                }
            }

            ins[i].arg1 = arg1;
            ins[i].arg2 = arg2;
            if (new_mode != ins[i].mode) {
                ins[i].mode = new_mode;
                changed = 1;
            }
        }

        if (!changed) {
            op_total = op_pos;
            arg_total = arg_pos;
            converged = 1;
            break;
        }
    }

    if (!converged) {
        PyErr_SetString(PyExc_RuntimeError, "m1logic coordinate solver did not converge");
        goto error;
    }

    encoded = PyBytes_FromStringAndSize(NULL, (Py_ssize_t)(op_total + arg_total));
    if (encoded == NULL) {
        goto error;
    }
    raw = (unsigned char *)PyBytes_AS_STRING(encoded);
    op_stream = raw;
    arg_stream = raw + op_total;

    op_i = 0;
    arg_i = 0;
    for (i = 0; i < ins_count; i++) {
        if (ins[i].mode == M1_MODE_MARKER_DEFAULT) {
            op_stream[op_i++] = (unsigned char)M1_MARKER_OPCODE;
            op_stream[op_i++] = (unsigned char)ins[i].custom_op;

            arg_stream[arg_i++] = (unsigned char)((ins[i].arg1 >> 8) & 0xFFU);
            arg_stream[arg_i++] = 0;
            arg_stream[arg_i++] = (unsigned char)(ins[i].arg1 & 0xFFU);
        }
        else if (ins[i].mode == M1_MODE_MARKER_SPECIAL) {
            op_stream[op_i++] = (unsigned char)M1_MARKER_OPCODE;
            op_stream[op_i++] = (unsigned char)ins[i].custom_op;

            arg_stream[arg_i++] = (unsigned char)((ins[i].arg1 >> 8) & 0xFFU);
            arg_stream[arg_i++] = (unsigned char)((ins[i].arg2 >> 8) & 0xFFU);
            arg_stream[arg_i++] = (unsigned char)(ins[i].arg1 & 0xFFU);
            arg_stream[arg_i++] = (unsigned char)(ins[i].arg2 & 0xFFU);
        }
        else {
            op_stream[op_i++] = (unsigned char)ins[i].custom_op;
            arg_stream[arg_i++] = (unsigned char)(ins[i].arg1 & 0xFFU);
            if (m1_custom_is_dual(ins[i].custom_op)) {
                arg_stream[arg_i++] = (unsigned char)(ins[i].arg2 & 0xFFU);
            }
        }
    }

    if (op_i != op_total || arg_i != arg_total) {
        PyErr_SetString(PyExc_RuntimeError, "m1logic encoder length mismatch");
        goto error;
    }

    *out_code = encoded;
    *out_split = op_total;
    PyMem_FREE(ins);
    return 1;

error:
    Py_XDECREF(encoded);
    PyMem_FREE(ins);
    return 0;
}

static int
m1_custom_marshal_enabled(void)
{
    static int initialized = 0;
    static int enabled = 0;
    const char *env;

    if (initialized) {
        return enabled;
    }

    initialized = 1;
    env = Py_GETENV("M1LOGIC_CUSTOM_MARSHAL");
    if (env != NULL && env[0] != '\0' && strcmp(env, "0") != 0) {
        enabled = 1;
    }
    return enabled;
}

static void
w_PyLong(const PyLongObject *ob, char flag, WFILE *p)
{
    Py_ssize_t i, j, n, l;
    digit d;

    W_TYPE(TYPE_LONG, p);
    if (Py_SIZE(ob) == 0) {
        w_long((long)0, p);
        return;
    }

    /* set l to number of base PyLong_MARSHAL_BASE digits */
    n = Py_ABS(Py_SIZE(ob));
    l = (n-1) * PyLong_MARSHAL_RATIO;
    d = ob->ob_digit[n-1];
    assert(d != 0); /* a PyLong is always normalized */
    do {
        d >>= PyLong_MARSHAL_SHIFT;
        l++;
    } while (d != 0);
    if (l > SIZE32_MAX) {
        p->depth--;
        p->error = WFERR_UNMARSHALLABLE;
        return;
    }
    w_long((long)(Py_SIZE(ob) > 0 ? l : -l), p);

    for (i=0; i < n-1; i++) {
        d = ob->ob_digit[i];
        for (j=0; j < PyLong_MARSHAL_RATIO; j++) {
            w_short(d & PyLong_MARSHAL_MASK, p);
            d >>= PyLong_MARSHAL_SHIFT;
        }
        assert (d == 0);
    }
    d = ob->ob_digit[n-1];
    do {
        w_short(d & PyLong_MARSHAL_MASK, p);
        d >>= PyLong_MARSHAL_SHIFT;
    } while (d != 0);
}

static int
w_ref(PyObject *v, char *flag, WFILE *p)
{
    _Py_hashtable_entry_t *entry;
    int w;

    if (p->version < 3 || p->hashtable == NULL)
        return 0; /* not writing object references */

    /* if it has only one reference, it definitely isn't shared */
    if (Py_REFCNT(v) == 1)
        return 0;

    entry = _Py_HASHTABLE_GET_ENTRY(p->hashtable, v);
    if (entry != NULL) {
        /* write the reference index to the stream */
        _Py_HASHTABLE_ENTRY_READ_DATA(p->hashtable, entry, w);
        /* we don't store "long" indices in the dict */
        assert(0 <= w && w <= 0x7fffffff);
        w_byte(TYPE_REF, p);
        w_long(w, p);
        return 1;
    } else {
        size_t s = p->hashtable->entries;
        /* we don't support long indices */
        if (s >= 0x7fffffff) {
            PyErr_SetString(PyExc_ValueError, "too many objects");
            goto err;
        }
        w = (int)s;
        Py_INCREF(v);
        if (_Py_HASHTABLE_SET(p->hashtable, v, w) < 0) {
            Py_DECREF(v);
            goto err;
        }
        *flag |= FLAG_REF;
        return 0;
    }
err:
    p->error = WFERR_UNMARSHALLABLE;
    return 1;
}

static void
w_complex_object(PyObject *v, char flag, WFILE *p);

static void
w_object(PyObject *v, WFILE *p)
{
    char flag = '\0';

    p->depth++;

    if (p->depth > MAX_MARSHAL_STACK_DEPTH) {
        p->error = WFERR_NESTEDTOODEEP;
    }
    else if (v == NULL) {
        w_byte(TYPE_NULL, p);
    }
    else if (v == Py_None) {
        w_byte(TYPE_NONE, p);
    }
    else if (v == PyExc_StopIteration) {
        w_byte(TYPE_STOPITER, p);
    }
    else if (v == Py_Ellipsis) {
        w_byte(TYPE_ELLIPSIS, p);
    }
    else if (v == Py_False) {
        w_byte(TYPE_FALSE, p);
    }
    else if (v == Py_True) {
        w_byte(TYPE_TRUE, p);
    }
    else if (!w_ref(v, &flag, p))
        w_complex_object(v, flag, p);

    p->depth--;
}

static void
w_complex_object(PyObject *v, char flag, WFILE *p)
{
    Py_ssize_t i, n;

    if (PyLong_CheckExact(v)) {
        long x = PyLong_AsLong(v);
        if ((x == -1)  && PyErr_Occurred()) {
            PyLongObject *ob = (PyLongObject *)v;
            PyErr_Clear();
            w_PyLong(ob, flag, p);
        }
        else {
#if SIZEOF_LONG > 4
            long y = Py_ARITHMETIC_RIGHT_SHIFT(long, x, 31);
            if (y && y != -1) {
                /* Too large for TYPE_INT */
                w_PyLong((PyLongObject*)v, flag, p);
            }
            else
#endif
            {
                W_TYPE(TYPE_INT, p);
                w_long(x, p);
            }
        }
    }
    else if (PyFloat_CheckExact(v)) {
        if (p->version > 1) {
            unsigned char buf[8];
            if (_PyFloat_Pack8(PyFloat_AsDouble(v),
                               buf, 1) < 0) {
                p->error = WFERR_UNMARSHALLABLE;
                return;
            }
            W_TYPE(TYPE_BINARY_FLOAT, p);
            w_string((char*)buf, 8, p);
        }
        else {
            char *buf = PyOS_double_to_string(PyFloat_AS_DOUBLE(v),
                                              'g', 17, 0, NULL);
            if (!buf) {
                p->error = WFERR_NOMEMORY;
                return;
            }
            n = strlen(buf);
            W_TYPE(TYPE_FLOAT, p);
            w_byte((int)n, p);
            w_string(buf, n, p);
            PyMem_Free(buf);
        }
    }
    else if (PyComplex_CheckExact(v)) {
        if (p->version > 1) {
            unsigned char buf[8];
            if (_PyFloat_Pack8(PyComplex_RealAsDouble(v),
                               buf, 1) < 0) {
                p->error = WFERR_UNMARSHALLABLE;
                return;
            }
            W_TYPE(TYPE_BINARY_COMPLEX, p);
            w_string((char*)buf, 8, p);
            if (_PyFloat_Pack8(PyComplex_ImagAsDouble(v),
                               buf, 1) < 0) {
                p->error = WFERR_UNMARSHALLABLE;
                return;
            }
            w_string((char*)buf, 8, p);
        }
        else {
            char *buf;
            W_TYPE(TYPE_COMPLEX, p);
            buf = PyOS_double_to_string(PyComplex_RealAsDouble(v),
                                        'g', 17, 0, NULL);
            if (!buf) {
                p->error = WFERR_NOMEMORY;
                return;
            }
            n = strlen(buf);
            w_byte((int)n, p);
            w_string(buf, n, p);
            PyMem_Free(buf);
            buf = PyOS_double_to_string(PyComplex_ImagAsDouble(v),
                                        'g', 17, 0, NULL);
            if (!buf) {
                p->error = WFERR_NOMEMORY;
                return;
            }
            n = strlen(buf);
            w_byte((int)n, p);
            w_string(buf, n, p);
            PyMem_Free(buf);
        }
    }
    else if (PyBytes_CheckExact(v)) {
        W_TYPE(TYPE_STRING, p);
        w_pstring(PyBytes_AS_STRING(v), PyBytes_GET_SIZE(v), p);
    }
    else if (PyUnicode_CheckExact(v)) {
        if (p->version >= 4 && PyUnicode_IS_ASCII(v)) {
            int is_short = PyUnicode_GET_LENGTH(v) < 256;
            if (is_short) {
                if (PyUnicode_CHECK_INTERNED(v))
                    W_TYPE(TYPE_SHORT_ASCII_INTERNED, p);
                else
                    W_TYPE(TYPE_SHORT_ASCII, p);
                w_short_pstring((char *) PyUnicode_1BYTE_DATA(v),
                                PyUnicode_GET_LENGTH(v), p);
            }
            else {
                if (PyUnicode_CHECK_INTERNED(v))
                    W_TYPE(TYPE_ASCII_INTERNED, p);
                else
                    W_TYPE(TYPE_ASCII, p);
                w_pstring((char *) PyUnicode_1BYTE_DATA(v),
                          PyUnicode_GET_LENGTH(v), p);
            }
        }
        else {
            PyObject *utf8;
            utf8 = PyUnicode_AsEncodedString(v, "utf8", "surrogatepass");
            if (utf8 == NULL) {
                p->depth--;
                p->error = WFERR_UNMARSHALLABLE;
                return;
            }
            if (p->version >= 3 &&  PyUnicode_CHECK_INTERNED(v))
                W_TYPE(TYPE_INTERNED, p);
            else
                W_TYPE(TYPE_UNICODE, p);
            w_pstring(PyBytes_AS_STRING(utf8), PyBytes_GET_SIZE(utf8), p);
            Py_DECREF(utf8);
        }
    }
    else if (PyTuple_CheckExact(v)) {
        n = PyTuple_Size(v);
        if (p->version >= 4 && n < 256) {
            W_TYPE(TYPE_SMALL_TUPLE, p);
            w_byte((unsigned char)n, p);
        }
        else {
            W_TYPE(TYPE_TUPLE, p);
            W_SIZE(n, p);
        }
        for (i = 0; i < n; i++) {
            w_object(PyTuple_GET_ITEM(v, i), p);
        }
    }
    else if (PyList_CheckExact(v)) {
        W_TYPE(TYPE_LIST, p);
        n = PyList_GET_SIZE(v);
        W_SIZE(n, p);
        for (i = 0; i < n; i++) {
            w_object(PyList_GET_ITEM(v, i), p);
        }
    }
    else if (PyDict_CheckExact(v)) {
        Py_ssize_t pos;
        PyObject *key, *value;
        W_TYPE(TYPE_DICT, p);
        /* This one is NULL object terminated! */
        pos = 0;
        while (PyDict_Next(v, &pos, &key, &value)) {
            w_object(key, p);
            w_object(value, p);
        }
        w_object((PyObject *)NULL, p);
    }
    else if (PyAnySet_CheckExact(v)) {
        PyObject *value, *it;

        if (PyObject_TypeCheck(v, &PySet_Type))
            W_TYPE(TYPE_SET, p);
        else
            W_TYPE(TYPE_FROZENSET, p);
        n = PyObject_Size(v);
        if (n == -1) {
            p->depth--;
            p->error = WFERR_UNMARSHALLABLE;
            return;
        }
        W_SIZE(n, p);
        it = PyObject_GetIter(v);
        if (it == NULL) {
            p->depth--;
            p->error = WFERR_UNMARSHALLABLE;
            return;
        }
        while ((value = PyIter_Next(it)) != NULL) {
            w_object(value, p);
            Py_DECREF(value);
        }
        Py_DECREF(it);
        if (PyErr_Occurred()) {
            p->depth--;
            p->error = WFERR_UNMARSHALLABLE;
            return;
        }
    }
    else if (PyCode_Check(v)) {
        PyCodeObject *co = (PyCodeObject *)v;
        PyObject *m1_code = NULL;
        int m1_split = 0;

        W_TYPE(TYPE_CODE, p);
        w_long(co->co_argcount, p);
        w_long(co->co_kwonlyargcount, p);
        w_long(co->co_nlocals, p);
        w_long(co->co_stacksize, p);
        w_long(co->co_flags, p);

        if (m1_custom_marshal_enabled()) {
            if (!m1_encode_code_bytes(co, &m1_code, &m1_split)) {
                p->depth--;
                if (PyErr_ExceptionMatches(PyExc_MemoryError)) {
                    p->error = WFERR_NOMEMORY;
                }
                else {
                    p->error = WFERR_UNMARSHALLABLE;
                }
                return;
            }

            w_long(m1_split, p);
            w_object(m1_code, p);
            Py_DECREF(m1_code);
        }
        else {
            w_object(co->co_code, p);
        }

        w_object(co->co_consts, p);
        w_object(co->co_names, p);
        w_object(co->co_varnames, p);
        w_object(co->co_freevars, p);
        w_object(co->co_cellvars, p);
        w_object(co->co_filename, p);
        w_object(co->co_name, p);
        w_long(co->co_firstlineno, p);
        w_object(co->co_lnotab, p);
    }
    else if (PyObject_CheckBuffer(v)) {
        /* Write unknown bytes-like objects as a bytes object */
        Py_buffer view;
        if (PyObject_GetBuffer(v, &view, PyBUF_SIMPLE) != 0) {
            w_byte(TYPE_UNKNOWN, p);
            p->depth--;
            p->error = WFERR_UNMARSHALLABLE;
            return;
        }
        W_TYPE(TYPE_STRING, p);
        w_pstring(view.buf, view.len, p);
        PyBuffer_Release(&view);
    }
    else {
        W_TYPE(TYPE_UNKNOWN, p);
        p->error = WFERR_UNMARSHALLABLE;
    }
}

static int
w_init_refs(WFILE *wf, int version)
{
    if (version >= 3) {
        wf->hashtable = _Py_hashtable_new(sizeof(PyObject *), sizeof(int),
                                          _Py_hashtable_hash_ptr,
                                          _Py_hashtable_compare_direct);
        if (wf->hashtable == NULL) {
            PyErr_NoMemory();
            return -1;
        }
    }
    return 0;
}

static int
w_decref_entry(_Py_hashtable_t *ht, _Py_hashtable_entry_t *entry,
               void *Py_UNUSED(data))
{
    PyObject *entry_key;

    _Py_HASHTABLE_ENTRY_READ_KEY(ht, entry, entry_key);
    Py_XDECREF(entry_key);
    return 0;
}

static void
w_clear_refs(WFILE *wf)
{
    if (wf->hashtable != NULL) {
        _Py_hashtable_foreach(wf->hashtable, w_decref_entry, NULL);
        _Py_hashtable_destroy(wf->hashtable);
    }
}

/* version currently has no effect for writing ints. */
void
PyMarshal_WriteLongToFile(long x, FILE *fp, int version)
{
    char buf[4];
    WFILE wf;
    memset(&wf, 0, sizeof(wf));
    wf.fp = fp;
    wf.ptr = wf.buf = buf;
    wf.end = wf.ptr + sizeof(buf);
    wf.error = WFERR_OK;
    wf.version = version;
    w_long(x, &wf);
    w_flush(&wf);
}

void
PyMarshal_WriteObjectToFile(PyObject *x, FILE *fp, int version)
{
    char buf[BUFSIZ];
    WFILE wf;
    memset(&wf, 0, sizeof(wf));
    wf.fp = fp;
    wf.ptr = wf.buf = buf;
    wf.end = wf.ptr + sizeof(buf);
    wf.error = WFERR_OK;
    wf.version = version;
    if (w_init_refs(&wf, version))
        return; /* caller mush check PyErr_Occurred() */
    w_object(x, &wf);
    w_clear_refs(&wf);
    w_flush(&wf);
}

typedef struct {
    FILE *fp;
    int depth;
    PyObject *readable;  /* Stream-like object being read from */
    PyObject *current_filename;
    char *ptr;
    char *end;
    char *buf;
    Py_ssize_t buf_size;
    PyObject *refs;  /* a list */
} RFILE;

static const char *
r_string(Py_ssize_t n, RFILE *p)
{
    Py_ssize_t read = -1;

    if (p->ptr != NULL) {
        /* Fast path for loads() */
        char *res = p->ptr;
        Py_ssize_t left = p->end - p->ptr;
        if (left < n) {
            PyErr_SetString(PyExc_EOFError,
                            "marshal data too short");
            return NULL;
        }
        p->ptr += n;
        return res;
    }
    if (p->buf == NULL) {
        p->buf = PyMem_MALLOC(n);
        if (p->buf == NULL) {
            PyErr_NoMemory();
            return NULL;
        }
        p->buf_size = n;
    }
    else if (p->buf_size < n) {
        p->buf = PyMem_REALLOC(p->buf, n);
        if (p->buf == NULL) {
            PyErr_NoMemory();
            return NULL;
        }
        p->buf_size = n;
    }

    if (!p->readable) {
        assert(p->fp != NULL);
        read = fread(p->buf, 1, n, p->fp);
    }
    else {
        _Py_IDENTIFIER(readinto);
        PyObject *res, *mview;
        Py_buffer buf;

        if (PyBuffer_FillInfo(&buf, NULL, p->buf, n, 0, PyBUF_CONTIG) == -1)
            return NULL;
        mview = PyMemoryView_FromBuffer(&buf);
        if (mview == NULL)
            return NULL;

        res = _PyObject_CallMethodId(p->readable, &PyId_readinto, "N", mview);
        if (res != NULL) {
            read = PyNumber_AsSsize_t(res, PyExc_ValueError);
            Py_DECREF(res);
        }
    }
    if (read != n) {
        if (!PyErr_Occurred()) {
            if (read > n)
                PyErr_Format(PyExc_ValueError,
                             "read() returned too much data: "
                             "%zd bytes requested, %zd returned",
                             n, read);
            else
                PyErr_SetString(PyExc_EOFError,
                                "EOF read where not expected");
        }
        return NULL;
    }
    return p->buf;
}

static int
r_byte(RFILE *p)
{
    int c = EOF;

    if (p->ptr != NULL) {
        if (p->ptr < p->end)
            c = (unsigned char) *p->ptr++;
        return c;
    }
    if (!p->readable) {
        assert(p->fp);
        c = getc(p->fp);
    }
    else {
        const char *ptr = r_string(1, p);
        if (ptr != NULL)
            c = *(unsigned char *) ptr;
    }
    return c;
}

static int
r_short(RFILE *p)
{
    short x = -1;
    const unsigned char *buffer;

    buffer = (const unsigned char *) r_string(2, p);
    if (buffer != NULL) {
        x = buffer[0];
        x |= buffer[1] << 8;
        /* Sign-extension, in case short greater than 16 bits */
        x |= -(x & 0x8000);
    }
    return x;
}

static long
r_long(RFILE *p)
{
    long x = -1;
    const unsigned char *buffer;

    buffer = (const unsigned char *) r_string(4, p);
    if (buffer != NULL) {
        x = buffer[0];
        x |= (long)buffer[1] << 8;
        x |= (long)buffer[2] << 16;
        x |= (long)buffer[3] << 24;
#if SIZEOF_LONG > 4
        /* Sign extension for 64-bit machines */
        x |= -(x & 0x80000000L);
#endif
    }
    return x;
}

static PyObject *
r_PyLong(RFILE *p)
{
    PyLongObject *ob;
    long n, size, i;
    int j, md, shorts_in_top_digit;
    digit d;

    n = r_long(p);
    if (PyErr_Occurred())
        return NULL;
    if (n == 0)
        return (PyObject *)_PyLong_New(0);
    if (n < -SIZE32_MAX || n > SIZE32_MAX) {
        PyErr_SetString(PyExc_ValueError,
                       "bad marshal data (long size out of range)");
        return NULL;
    }

    size = 1 + (Py_ABS(n) - 1) / PyLong_MARSHAL_RATIO;
    shorts_in_top_digit = 1 + (Py_ABS(n) - 1) % PyLong_MARSHAL_RATIO;
    ob = _PyLong_New(size);
    if (ob == NULL)
        return NULL;

    Py_SIZE(ob) = n > 0 ? size : -size;

    for (i = 0; i < size-1; i++) {
        d = 0;
        for (j=0; j < PyLong_MARSHAL_RATIO; j++) {
            md = r_short(p);
            if (PyErr_Occurred()) {
                Py_DECREF(ob);
                return NULL;
            }
            if (md < 0 || md > PyLong_MARSHAL_BASE)
                goto bad_digit;
            d += (digit)md << j*PyLong_MARSHAL_SHIFT;
        }
        ob->ob_digit[i] = d;
    }

    d = 0;
    for (j=0; j < shorts_in_top_digit; j++) {
        md = r_short(p);
        if (PyErr_Occurred()) {
            Py_DECREF(ob);
            return NULL;
        }
        if (md < 0 || md > PyLong_MARSHAL_BASE)
            goto bad_digit;
        /* topmost marshal digit should be nonzero */
        if (md == 0 && j == shorts_in_top_digit - 1) {
            Py_DECREF(ob);
            PyErr_SetString(PyExc_ValueError,
                "bad marshal data (unnormalized long data)");
            return NULL;
        }
        d += (digit)md << j*PyLong_MARSHAL_SHIFT;
    }
    if (PyErr_Occurred()) {
        Py_DECREF(ob);
        return NULL;
    }
    /* top digit should be nonzero, else the resulting PyLong won't be
       normalized */
    ob->ob_digit[size-1] = d;
    return (PyObject *)ob;
  bad_digit:
    Py_DECREF(ob);
    PyErr_SetString(PyExc_ValueError,
                    "bad marshal data (digit out of range in long)");
    return NULL;
}

/* allocate the reflist index for a new object. Return -1 on failure */
static Py_ssize_t
r_ref_reserve(int flag, RFILE *p)
{
    if (flag) { /* currently only FLAG_REF is defined */
        Py_ssize_t idx = PyList_GET_SIZE(p->refs);
        if (idx >= 0x7ffffffe) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (index list too large)");
            return -1;
        }
        if (PyList_Append(p->refs, Py_None) < 0)
            return -1;
        return idx;
    } else
        return 0;
}

/* insert the new object 'o' to the reflist at previously
 * allocated index 'idx'.
 * 'o' can be NULL, in which case nothing is done.
 * if 'o' was non-NULL, and the function succeeds, 'o' is returned.
 * if 'o' was non-NULL, and the function fails, 'o' is released and
 * NULL returned. This simplifies error checking at the call site since
 * a single test for NULL for the function result is enough.
 */
static PyObject *
r_ref_insert(PyObject *o, Py_ssize_t idx, int flag, RFILE *p)
{
    if (o != NULL && flag) { /* currently only FLAG_REF is defined */
        PyObject *tmp = PyList_GET_ITEM(p->refs, idx);
        Py_INCREF(o);
        PyList_SET_ITEM(p->refs, idx, o);
        Py_DECREF(tmp);
    }
    return o;
}

/* combination of both above, used when an object can be
 * created whenever it is seen in the file, as opposed to
 * after having loaded its sub-objects.
 */
static PyObject *
r_ref(PyObject *o, int flag, RFILE *p)
{
    assert(flag & FLAG_REF);
    if (o == NULL)
        return NULL;
    if (PyList_Append(p->refs, o) < 0) {
        Py_DECREF(o); /* release the new object */
        return NULL;
    }
    return o;
}

static PyObject *
r_object(RFILE *p)
{
    /* NULL is a valid return value, it does not necessarily means that
       an exception is set. */
    PyObject *v, *v2;
    Py_ssize_t idx = 0;
    long i, n;
    int type, code = r_byte(p);
    int flag, is_interned = 0;
    PyObject *retval = NULL;

    if (code == EOF) {
        PyErr_SetString(PyExc_EOFError,
                        "EOF read where object expected");
        return NULL;
    }

    p->depth++;

    if (p->depth > MAX_MARSHAL_STACK_DEPTH) {
        p->depth--;
        PyErr_SetString(PyExc_ValueError, "recursion limit exceeded");
        return NULL;
    }

    flag = code & FLAG_REF;
    type = code & ~FLAG_REF;

#define R_REF(O) do{\
    if (flag) \
        O = r_ref(O, flag, p);\
} while (0)

    switch (type) {

    case TYPE_NULL:
        break;

    case TYPE_NONE:
        Py_INCREF(Py_None);
        retval = Py_None;
        break;

    case TYPE_STOPITER:
        Py_INCREF(PyExc_StopIteration);
        retval = PyExc_StopIteration;
        break;

    case TYPE_ELLIPSIS:
        Py_INCREF(Py_Ellipsis);
        retval = Py_Ellipsis;
        break;

    case TYPE_FALSE:
        Py_INCREF(Py_False);
        retval = Py_False;
        break;

    case TYPE_TRUE:
        Py_INCREF(Py_True);
        retval = Py_True;
        break;

    case TYPE_INT:
        n = r_long(p);
        retval = PyErr_Occurred() ? NULL : PyLong_FromLong(n);
        R_REF(retval);
        break;

    case TYPE_LONG:
        retval = r_PyLong(p);
        R_REF(retval);
        break;

    case TYPE_FLOAT:
        {
            char buf[256];
            const char *ptr;
            double dx;
            n = r_byte(p);
            if (n == EOF) {
                PyErr_SetString(PyExc_EOFError,
                    "EOF read where object expected");
                break;
            }
            ptr = r_string(n, p);
            if (ptr == NULL)
                break;
            memcpy(buf, ptr, n);
            buf[n] = '\0';
            dx = PyOS_string_to_double(buf, NULL, NULL);
            if (dx == -1.0 && PyErr_Occurred())
                break;
            retval = PyFloat_FromDouble(dx);
            R_REF(retval);
            break;
        }

    case TYPE_BINARY_FLOAT:
        {
            const unsigned char *buf;
            double x;
            buf = (const unsigned char *) r_string(8, p);
            if (buf == NULL)
                break;
            x = _PyFloat_Unpack8(buf, 1);
            if (x == -1.0 && PyErr_Occurred())
                break;
            retval = PyFloat_FromDouble(x);
            R_REF(retval);
            break;
        }

    case TYPE_COMPLEX:
        {
            char buf[256];
            const char *ptr;
            Py_complex c;
            n = r_byte(p);
            if (n == EOF) {
                PyErr_SetString(PyExc_EOFError,
                    "EOF read where object expected");
                break;
            }
            ptr = r_string(n, p);
            if (ptr == NULL)
                break;
            memcpy(buf, ptr, n);
            buf[n] = '\0';
            c.real = PyOS_string_to_double(buf, NULL, NULL);
            if (c.real == -1.0 && PyErr_Occurred())
                break;
            n = r_byte(p);
            if (n == EOF) {
                PyErr_SetString(PyExc_EOFError,
                    "EOF read where object expected");
                break;
            }
            ptr = r_string(n, p);
            if (ptr == NULL)
                break;
            memcpy(buf, ptr, n);
            buf[n] = '\0';
            c.imag = PyOS_string_to_double(buf, NULL, NULL);
            if (c.imag == -1.0 && PyErr_Occurred())
                break;
            retval = PyComplex_FromCComplex(c);
            R_REF(retval);
            break;
        }

    case TYPE_BINARY_COMPLEX:
        {
            const unsigned char *buf;
            Py_complex c;
            buf = (const unsigned char *) r_string(8, p);
            if (buf == NULL)
                break;
            c.real = _PyFloat_Unpack8(buf, 1);
            if (c.real == -1.0 && PyErr_Occurred())
                break;
            buf = (const unsigned char *) r_string(8, p);
            if (buf == NULL)
                break;
            c.imag = _PyFloat_Unpack8(buf, 1);
            if (c.imag == -1.0 && PyErr_Occurred())
                break;
            retval = PyComplex_FromCComplex(c);
            R_REF(retval);
            break;
        }

    case TYPE_STRING:
        {
            const char *ptr;
            n = r_long(p);
            if (PyErr_Occurred())
                break;
            if (n < 0 || n > SIZE32_MAX) {
                PyErr_SetString(PyExc_ValueError, "bad marshal data (bytes object size out of range)");
                break;
            }
            v = PyBytes_FromStringAndSize((char *)NULL, n);
            if (v == NULL)
                break;
            ptr = r_string(n, p);
            if (ptr == NULL) {
                Py_DECREF(v);
                break;
            }
            memcpy(PyBytes_AS_STRING(v), ptr, n);
            retval = v;
            R_REF(retval);
            break;
        }

    case TYPE_ASCII_INTERNED:
        is_interned = 1;
        /* fall through */
    case TYPE_ASCII:
        n = r_long(p);
        if (PyErr_Occurred())
            break;
        if (n < 0 || n > SIZE32_MAX) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (string size out of range)");
            break;
        }
        goto _read_ascii;

    case TYPE_SHORT_ASCII_INTERNED:
        is_interned = 1;
        /* fall through */
    case TYPE_SHORT_ASCII:
        n = r_byte(p);
        if (n == EOF) {
            PyErr_SetString(PyExc_EOFError,
                "EOF read where object expected");
            break;
        }
    _read_ascii:
        {
            const char *ptr;
            ptr = r_string(n, p);
            if (ptr == NULL)
                break;
            v = PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND, ptr, n);
            if (v == NULL)
                break;
            if (is_interned)
                PyUnicode_InternInPlace(&v);
            retval = v;
            R_REF(retval);
            break;
        }

    case TYPE_INTERNED:
        is_interned = 1;
        /* fall through */
    case TYPE_UNICODE:
        {
        const char *buffer;

        n = r_long(p);
        if (PyErr_Occurred())
            break;
        if (n < 0 || n > SIZE32_MAX) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (string size out of range)");
            break;
        }
        if (n != 0) {
            buffer = r_string(n, p);
            if (buffer == NULL)
                break;
            v = PyUnicode_DecodeUTF8(buffer, n, "surrogatepass");
        }
        else {
            v = PyUnicode_New(0, 0);
        }
        if (v == NULL)
            break;
        if (is_interned)
            PyUnicode_InternInPlace(&v);
        retval = v;
        R_REF(retval);
        break;
        }

    case TYPE_SMALL_TUPLE:
        n = (unsigned char) r_byte(p);
        if (PyErr_Occurred())
            break;
        goto _read_tuple;
    case TYPE_TUPLE:
        n = r_long(p);
        if (PyErr_Occurred())
            break;
        if (n < 0 || n > SIZE32_MAX) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (tuple size out of range)");
            break;
        }
    _read_tuple:
        v = PyTuple_New(n);
        R_REF(v);
        if (v == NULL)
            break;

        for (i = 0; i < n; i++) {
            v2 = r_object(p);
            if ( v2 == NULL ) {
                if (!PyErr_Occurred())
                    PyErr_SetString(PyExc_TypeError,
                        "NULL object in marshal data for tuple");
                Py_DECREF(v);
                v = NULL;
                break;
            }
            PyTuple_SET_ITEM(v, i, v2);
        }
        retval = v;
        break;

    case TYPE_LIST:
        n = r_long(p);
        if (PyErr_Occurred())
            break;
        if (n < 0 || n > SIZE32_MAX) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (list size out of range)");
            break;
        }
        v = PyList_New(n);
        R_REF(v);
        if (v == NULL)
            break;
        for (i = 0; i < n; i++) {
            v2 = r_object(p);
            if ( v2 == NULL ) {
                if (!PyErr_Occurred())
                    PyErr_SetString(PyExc_TypeError,
                        "NULL object in marshal data for list");
                Py_DECREF(v);
                v = NULL;
                break;
            }
            PyList_SET_ITEM(v, i, v2);
        }
        retval = v;
        break;

    case TYPE_DICT:
        v = PyDict_New();
        R_REF(v);
        if (v == NULL)
            break;
        for (;;) {
            PyObject *key, *val;
            key = r_object(p);
            if (key == NULL)
                break;
            val = r_object(p);
            if (val == NULL) {
                Py_DECREF(key);
                break;
            }
            if (PyDict_SetItem(v, key, val) < 0) {
                Py_DECREF(key);
                Py_DECREF(val);
                break;
            }
            Py_DECREF(key);
            Py_DECREF(val);
        }
        if (PyErr_Occurred()) {
            Py_DECREF(v);
            v = NULL;
        }
        retval = v;
        break;

    case TYPE_SET:
    case TYPE_FROZENSET:
        n = r_long(p);
        if (PyErr_Occurred())
            break;
        if (n < 0 || n > SIZE32_MAX) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (set size out of range)");
            break;
        }

        if (n == 0 && type == TYPE_FROZENSET) {
            /* call frozenset() to get the empty frozenset singleton */
            v = PyObject_CallFunction((PyObject*)&PyFrozenSet_Type, NULL);
            if (v == NULL)
                break;
            R_REF(v);
            retval = v;
        }
        else {
            v = (type == TYPE_SET) ? PySet_New(NULL) : PyFrozenSet_New(NULL);
            if (type == TYPE_SET) {
                R_REF(v);
            } else {
                /* must use delayed registration of frozensets because they must
                 * be init with a refcount of 1
                 */
                idx = r_ref_reserve(flag, p);
                if (idx < 0)
                    Py_CLEAR(v); /* signal error */
            }
            if (v == NULL)
                break;

            for (i = 0; i < n; i++) {
                v2 = r_object(p);
                if ( v2 == NULL ) {
                    if (!PyErr_Occurred())
                        PyErr_SetString(PyExc_TypeError,
                            "NULL object in marshal data for set");
                    Py_DECREF(v);
                    v = NULL;
                    break;
                }
                if (PySet_Add(v, v2) == -1) {
                    Py_DECREF(v);
                    Py_DECREF(v2);
                    v = NULL;
                    break;
                }
                Py_DECREF(v2);
            }
            if (type != TYPE_SET)
                v = r_ref_insert(v, idx, flag, p);
            retval = v;
        }
        break;

    case TYPE_CODE:
        {
            int argcount;
            int kwonlyargcount;
            int nlocals;
            int stacksize;
            int flags;
            PyObject *code = NULL;
            PyObject *consts = NULL;
            PyObject *names = NULL;
            PyObject *varnames = NULL;
            PyObject *freevars = NULL;
            PyObject *cellvars = NULL;
            PyObject *filename = NULL;
            PyObject *name = NULL;
            int firstlineno;
            PyObject *lnotab = NULL;

            idx = r_ref_reserve(flag, p);
            if (idx < 0)
                break;

            v = NULL;

            /* XXX ignore long->int overflows for now */
            argcount = (int)r_long(p);
            if (PyErr_Occurred())
                goto code_error;
            kwonlyargcount = (int)r_long(p);
            if (PyErr_Occurred())
                goto code_error;
            nlocals = (int)r_long(p);
            if (PyErr_Occurred())
                goto code_error;
            stacksize = (int)r_long(p);
            if (PyErr_Occurred())
                goto code_error;
            flags = (int)r_long(p);
            if (PyErr_Occurred())
                goto code_error;
            code = r_object(p);
            if (code == NULL)
                goto code_error;
            consts = r_object(p);
            if (consts == NULL)
                goto code_error;
            names = r_object(p);
            if (names == NULL)
                goto code_error;
            varnames = r_object(p);
            if (varnames == NULL)
                goto code_error;
            freevars = r_object(p);
            if (freevars == NULL)
                goto code_error;
            cellvars = r_object(p);
            if (cellvars == NULL)
                goto code_error;
            filename = r_object(p);
            if (filename == NULL)
                goto code_error;
            if (PyUnicode_CheckExact(filename)) {
                if (p->current_filename != NULL) {
                    if (!PyUnicode_Compare(filename, p->current_filename)) {
                        Py_DECREF(filename);
                        Py_INCREF(p->current_filename);
                        filename = p->current_filename;
                    }
                }
                else {
                    p->current_filename = filename;
                }
            }
            name = r_object(p);
            if (name == NULL)
                goto code_error;
            firstlineno = (int)r_long(p);
            if (firstlineno == -1 && PyErr_Occurred())
                break;
            lnotab = r_object(p);
            if (lnotab == NULL)
                goto code_error;

            v = (PyObject *) PyCode_New(
                            argcount, kwonlyargcount,
                            nlocals, stacksize, flags,
                            code, consts, names, varnames,
                            freevars, cellvars, filename, name,
                            firstlineno, lnotab);
            v = r_ref_insert(v, idx, flag, p);

          code_error:
            Py_XDECREF(code);
            Py_XDECREF(consts);
            Py_XDECREF(names);
            Py_XDECREF(varnames);
            Py_XDECREF(freevars);
            Py_XDECREF(cellvars);
            Py_XDECREF(filename);
            Py_XDECREF(name);
            Py_XDECREF(lnotab);
        }
        retval = v;
        break;

    case TYPE_REF:
        n = r_long(p);
        if (n < 0 || n >= PyList_GET_SIZE(p->refs)) {
            if (n == -1 && PyErr_Occurred())
                break;
            PyErr_SetString(PyExc_ValueError, "bad marshal data (invalid reference)");
            break;
        }
        v = PyList_GET_ITEM(p->refs, n);
        if (v == Py_None) {
            PyErr_SetString(PyExc_ValueError, "bad marshal data (invalid reference)");
            break;
        }
        Py_INCREF(v);
        retval = v;
        break;

    default:
        /* Bogus data got written, which isn't ideal.
           This will let you keep working and recover. */
        PyErr_SetString(PyExc_ValueError, "bad marshal data (unknown type code)");
        break;

    }
    p->depth--;
    return retval;
}

static PyObject *
read_object(RFILE *p)
{
    PyObject *v;
    if (PyErr_Occurred()) {
        fprintf(stderr, "XXX readobject called with exception set\n");
        return NULL;
    }
    v = r_object(p);
    if (v == NULL && !PyErr_Occurred())
        PyErr_SetString(PyExc_TypeError, "NULL object in marshal data for object");
    return v;
}

int
PyMarshal_ReadShortFromFile(FILE *fp)
{
    RFILE rf;
    int res;
    assert(fp);
    rf.readable = NULL;
    rf.fp = fp;
    rf.current_filename = NULL;
    rf.end = rf.ptr = NULL;
    rf.buf = NULL;
    res = r_short(&rf);
    if (rf.buf != NULL)
        PyMem_FREE(rf.buf);
    return res;
}

long
PyMarshal_ReadLongFromFile(FILE *fp)
{
    RFILE rf;
    long res;
    rf.fp = fp;
    rf.readable = NULL;
    rf.current_filename = NULL;
    rf.ptr = rf.end = NULL;
    rf.buf = NULL;
    res = r_long(&rf);
    if (rf.buf != NULL)
        PyMem_FREE(rf.buf);
    return res;
}

/* Return size of file in bytes; < 0 if unknown or INT_MAX if too big */
static off_t
getfilesize(FILE *fp)
{
    struct _Py_stat_struct st;
    if (_Py_fstat_noraise(fileno(fp), &st) != 0)
        return -1;
#if SIZEOF_OFF_T == 4
    else if (st.st_size >= INT_MAX)
        return (off_t)INT_MAX;
#endif
    else
        return (off_t)st.st_size;
}

/* If we can get the size of the file up-front, and it's reasonably small,
 * read it in one gulp and delegate to ...FromString() instead.  Much quicker
 * than reading a byte at a time from file; speeds .pyc imports.
 * CAUTION:  since this may read the entire remainder of the file, don't
 * call it unless you know you're done with the file.
 */
PyObject *
PyMarshal_ReadLastObjectFromFile(FILE *fp)
{
/* REASONABLE_FILE_LIMIT is by defn something big enough for Tkinter.pyc. */
#define REASONABLE_FILE_LIMIT (1L << 18)
    off_t filesize;
    filesize = getfilesize(fp);
    if (filesize > 0 && filesize <= REASONABLE_FILE_LIMIT) {
        char* pBuf = (char *)PyMem_MALLOC(filesize);
        if (pBuf != NULL) {
            size_t n = fread(pBuf, 1, (size_t)filesize, fp);
            PyObject* v = PyMarshal_ReadObjectFromString(pBuf, n);
            PyMem_FREE(pBuf);
            return v;
        }

    }
    /* We don't have fstat, or we do but the file is larger than
     * REASONABLE_FILE_LIMIT or malloc failed -- read a byte at a time.
     */
    return PyMarshal_ReadObjectFromFile(fp);

#undef REASONABLE_FILE_LIMIT
}

PyObject *
PyMarshal_ReadObjectFromFile(FILE *fp)
{
    RFILE rf;
    PyObject *result;
    rf.fp = fp;
    rf.readable = NULL;
    rf.current_filename = NULL;
    rf.depth = 0;
    rf.ptr = rf.end = NULL;
    rf.buf = NULL;
    rf.refs = PyList_New(0);
    if (rf.refs == NULL)
        return NULL;
    result = r_object(&rf);
    Py_DECREF(rf.refs);
    if (rf.buf != NULL)
        PyMem_FREE(rf.buf);
    return result;
}

PyObject *
PyMarshal_ReadObjectFromString(const char *str, Py_ssize_t len)
{
    RFILE rf;
    PyObject *result;
    rf.fp = NULL;
    rf.readable = NULL;
    rf.current_filename = NULL;
    rf.ptr = (char *)str;
    rf.end = (char *)str + len;
    rf.buf = NULL;
    rf.depth = 0;
    rf.refs = PyList_New(0);
    if (rf.refs == NULL)
        return NULL;
    result = r_object(&rf);
    Py_DECREF(rf.refs);
    if (rf.buf != NULL)
        PyMem_FREE(rf.buf);
    return result;
}

PyObject *
PyMarshal_WriteObjectToString(PyObject *x, int version)
{
    WFILE wf;

    memset(&wf, 0, sizeof(wf));
    wf.str = PyBytes_FromStringAndSize((char *)NULL, 50);
    if (wf.str == NULL)
        return NULL;
    wf.ptr = wf.buf = PyBytes_AS_STRING((PyBytesObject *)wf.str);
    wf.end = wf.ptr + PyBytes_Size(wf.str);
    wf.error = WFERR_OK;
    wf.version = version;
    if (w_init_refs(&wf, version)) {
        Py_DECREF(wf.str);
        return NULL;
    }
    w_object(x, &wf);
    w_clear_refs(&wf);
    if (wf.str != NULL) {
        char *base = PyBytes_AS_STRING((PyBytesObject *)wf.str);
        if (wf.ptr - base > PY_SSIZE_T_MAX) {
            Py_DECREF(wf.str);
            PyErr_SetString(PyExc_OverflowError,
                            "too much marshal data for a bytes object");
            return NULL;
        }
        if (_PyBytes_Resize(&wf.str, (Py_ssize_t)(wf.ptr - base)) < 0)
            return NULL;
    }
    if (wf.error != WFERR_OK) {
        Py_XDECREF(wf.str);
        if (wf.error == WFERR_NOMEMORY)
            PyErr_NoMemory();
        else
            PyErr_SetString(PyExc_ValueError,
              (wf.error==WFERR_UNMARSHALLABLE)?"unmarshallable object"
               :"object too deeply nested to marshal");
        return NULL;
    }
    return wf.str;
}

/* And an interface for Python programs... */

static PyObject *
marshal_dump(PyObject *self, PyObject *args)
{
    /* XXX Quick hack -- need to do this differently */
    PyObject *x;
    PyObject *f;
    int version = Py_MARSHAL_VERSION;
    PyObject *s;
    PyObject *res;
    _Py_IDENTIFIER(write);

    if (!PyArg_ParseTuple(args, "OO|i:dump", &x, &f, &version))
        return NULL;
    s = PyMarshal_WriteObjectToString(x, version);
    if (s == NULL)
        return NULL;
    res = _PyObject_CallMethodId(f, &PyId_write, "O", s);
    Py_DECREF(s);
    return res;
}

PyDoc_STRVAR(dump_doc,
"dump(value, file[, version])\n\
\n\
Write the value on the open file. The value must be a supported type.\n\
The file must be a writeable binary file.\n\
\n\
If the value has (or contains an object that has) an unsupported type, a\n\
ValueError exception is raised - but garbage data will also be written\n\
to the file. The object will not be properly read back by load()\n\
\n\
The version argument indicates the data format that dump should use.");

static PyObject *
marshal_load(PyObject *self, PyObject *f)
{
    PyObject *data, *result;
    _Py_IDENTIFIER(read);
    RFILE rf;

    /*
     * Make a call to the read method, but read zero bytes.
     * This is to ensure that the object passed in at least
     * has a read method which returns bytes.
     * This can be removed if we guarantee good error handling
     * for r_string()
     */
    data = _PyObject_CallMethodId(f, &PyId_read, "i", 0);
    if (data == NULL)
        return NULL;
    if (!PyBytes_Check(data)) {
        PyErr_Format(PyExc_TypeError,
                     "f.read() returned not bytes but %.100s",
                     data->ob_type->tp_name);
        result = NULL;
    }
    else {
        rf.depth = 0;
        rf.fp = NULL;
        rf.readable = f;
        rf.current_filename = NULL;
        rf.ptr = rf.end = NULL;
        rf.buf = NULL;
        if ((rf.refs = PyList_New(0)) != NULL) {
            result = read_object(&rf);
            Py_DECREF(rf.refs);
            if (rf.buf != NULL)
                PyMem_FREE(rf.buf);
        } else
            result = NULL;
    }
    Py_DECREF(data);
    return result;
}

PyDoc_STRVAR(load_doc,
"load(file)\n\
\n\
Read one value from the open file and return it. If no valid value is\n\
read (e.g. because the data has a different Python version's\n\
incompatible marshal format), raise EOFError, ValueError or TypeError.\n\
The file must be a readable binary file.\n\
\n\
Note: If an object containing an unsupported type was marshalled with\n\
dump(), load() will substitute None for the unmarshallable type.");


static PyObject *
marshal_dumps(PyObject *self, PyObject *args)
{
    PyObject *x;
    int version = Py_MARSHAL_VERSION;
    if (!PyArg_ParseTuple(args, "O|i:dumps", &x, &version))
        return NULL;
    return PyMarshal_WriteObjectToString(x, version);
}

PyDoc_STRVAR(dumps_doc,
"dumps(value[, version])\n\
\n\
Return the bytes object that would be written to a file by dump(value, file).\n\
The value must be a supported type. Raise a ValueError exception if\n\
value has (or contains an object that has) an unsupported type.\n\
\n\
The version argument indicates the data format that dumps should use.");


static PyObject *
marshal_loads(PyObject *self, PyObject *args)
{
    RFILE rf;
    Py_buffer p;
    char *s;
    Py_ssize_t n;
    PyObject* result;
    if (!PyArg_ParseTuple(args, "y*:loads", &p))
        return NULL;
    s = p.buf;
    n = p.len;
    rf.fp = NULL;
    rf.readable = NULL;
    rf.current_filename = NULL;
    rf.ptr = s;
    rf.end = s + n;
    rf.depth = 0;
    if ((rf.refs = PyList_New(0)) == NULL)
        return NULL;
    result = read_object(&rf);
    PyBuffer_Release(&p);
    Py_DECREF(rf.refs);
    return result;
}

PyDoc_STRVAR(loads_doc,
"loads(bytes)\n\
\n\
Convert the bytes-like object to a value. If no valid value is found,\n\
raise EOFError, ValueError or TypeError. Extra bytes in the input are\n\
ignored.");

static PyMethodDef marshal_methods[] = {
    {"dump",            marshal_dump,   METH_VARARGS,   dump_doc},
    {"load",            marshal_load,   METH_O,         load_doc},
    {"dumps",           marshal_dumps,  METH_VARARGS,   dumps_doc},
    {"loads",           marshal_loads,  METH_VARARGS,   loads_doc},
    {NULL,              NULL}           /* sentinel */
};


PyDoc_STRVAR(module_doc,
"This module contains functions that can read and write Python values in\n\
a binary format. The format is specific to Python, but independent of\n\
machine architecture issues.\n\
\n\
Not all Python object types are supported; in general, only objects\n\
whose value is independent from a particular invocation of Python can be\n\
written and read by this module. The following types are supported:\n\
None, integers, floating point numbers, strings, bytes, bytearrays,\n\
tuples, lists, sets, dictionaries, and code objects, where it\n\
should be understood that tuples, lists and dictionaries are only\n\
supported as long as the values contained therein are themselves\n\
supported; and recursive lists and dictionaries should not be written\n\
(they will cause infinite loops).\n\
\n\
Variables:\n\
\n\
version -- indicates the format that the module uses. Version 0 is the\n\
    historical format, version 1 shares interned strings and version 2\n\
    uses a binary format for floating point numbers.\n\
    Version 3 shares common object references (New in version 3.4).\n\
\n\
Functions:\n\
\n\
dump() -- write value to a file\n\
load() -- read value from a file\n\
dumps() -- marshal value as a bytes object\n\
loads() -- read value from a bytes-like object");



static struct PyModuleDef marshalmodule = {
    PyModuleDef_HEAD_INIT,
    "marshal",
    module_doc,
    0,
    marshal_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyMarshal_Init(void)
{
    PyObject *mod = PyModule_Create(&marshalmodule);
    if (mod == NULL)
        return NULL;
    PyModule_AddIntConstant(mod, "version", Py_MARSHAL_VERSION);
    return mod;
}
