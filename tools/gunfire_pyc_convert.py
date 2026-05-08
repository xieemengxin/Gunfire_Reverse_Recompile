#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gunfire 自定义 pyc -> 标准 pyc 转换脚本。

主要功能:
- 使用 `opcode_map.json` 把乱序 opcode 还原成标准 Python 3.6 opcode
- 支持按 `co_filename` 还原更接近源码的输出目录结构

常用示例:
    python3.6 tools/gunfire_pyc_convert.py convert-dir \
        --in-dir extracted/extracted_data1 \
        --out-dir converted/converted_data1 \
        --map-json tools/opcode_map.json \
        --real-names

    python3 tools/gunfire_pyc_convert.py list-names --in-dir extracted/extracted_data1

说明:
    `convert-file` / `convert-dir` 建议使用 Python 3.6 运行，
    因为最终输出的是 Python 3.6 pyc。
"""
from __future__ import print_function

import argparse
import collections
import concurrent.futures
import json
import marshal
import os
from pathlib import Path
import struct
import sys
import types

try:
    from xdis.opcodes import opcode_36 as _op36
except Exception:
    _op36 = None

try:
    from xdis import magics as _xdis_magics
except Exception:
    _xdis_magics = None


FLAG_REF = 0x80

TYPE_NULL = "0"
TYPE_NONE = "N"
TYPE_FALSE = "F"
TYPE_TRUE = "T"
TYPE_STOPITER = "S"
TYPE_ELLIPSIS = "."
TYPE_INT = "i"
TYPE_INT64 = "I"
TYPE_LONG = "l"
TYPE_FLOAT = "f"
TYPE_BINARY_FLOAT = "g"
TYPE_COMPLEX = "x"
TYPE_BINARY_COMPLEX = "y"
TYPE_STRING = "s"
TYPE_INTERNED = "t"
TYPE_REF = "r"
TYPE_TUPLE = "("
TYPE_LIST = "["
TYPE_DICT = "{"
TYPE_CODE = "c"
TYPE_UNICODE = "u"
TYPE_SET = "<"
TYPE_FROZENSET = ">"
TYPE_ASCII = "a"
TYPE_ASCII_INTERNED = "A"
TYPE_SMALL_TUPLE = ")"
TYPE_SHORT_ASCII = "z"
TYPE_SHORT_ASCII_INTERNED = "Z"

MARKER_OPCODE = 118
HAVE_ARGUMENT = int(getattr(_op36, "HAVE_ARGUMENT", 90))
EXTENDED_ARG = int(getattr(_op36, "EXTENDED_ARG", 144))

_FALLBACK_STD_HAS_JABS = set([111, 112, 113, 114, 115, 119])
_FALLBACK_STD_HAS_JREL = set([93, 110, 120, 121, 122, 143, 154])

if _op36 is not None:
    STD_HAS_JABS = set(int(x) for x in getattr(_op36, "hasjabs", []))
    STD_HAS_JREL = set(int(x) for x in getattr(_op36, "hasjrel", []))
else:
    STD_HAS_JABS = set(_FALLBACK_STD_HAS_JABS)
    STD_HAS_JREL = set(_FALLBACK_STD_HAS_JREL)

if _xdis_magics is not None:
    MAGIC36 = bytes(_xdis_magics.by_version.get("3.6", b"3\r\r\n"))
else:
    MAGIC36 = b"3\r\r\n"

# From evalframe analysis (sub_1800AE0A0).
DUAL_ARG_OPS = set([110, 136, 140, 151, 173, 185, 195, 197, 208, 217, 220, 236, 240])
MARKER_SPECIAL_NEXT = set([110, 136, 140, 151, 173, 185, 195, 197, 208, 217, 220, 236, 240])
DUAL_ABS_OPS = set([110, 140, 151, 197, 217, 240])
DUAL_REL_OPS = set([136, 173, 185, 195, 208, 220, 236])

NULL_SENTINEL = object()


class CustomCode(object):
    __slots__ = (
        "co_argcount",
        "co_kwonlyargcount",
        "co_nlocals",
        "co_stacksize",
        "co_flags",
        "co_custom_split",
        "co_code",
        "co_consts",
        "co_names",
        "co_varnames",
        "co_freevars",
        "co_cellvars",
        "co_filename",
        "co_name",
        "co_firstlineno",
        "co_lnotab",
    )

    def __init__(
        self,
        co_argcount,
        co_kwonlyargcount,
        co_nlocals,
        co_stacksize,
        co_flags,
        co_custom_split,
        co_code,
        co_consts,
        co_names,
        co_varnames,
        co_freevars,
        co_cellvars,
        co_filename,
        co_name,
        co_firstlineno,
        co_lnotab,
    ):
        self.co_argcount = co_argcount
        self.co_kwonlyargcount = co_kwonlyargcount
        self.co_nlocals = co_nlocals
        self.co_stacksize = co_stacksize
        self.co_flags = co_flags
        self.co_custom_split = co_custom_split
        self.co_code = co_code
        self.co_consts = co_consts
        self.co_names = co_names
        self.co_varnames = co_varnames
        self.co_freevars = co_freevars
        self.co_cellvars = co_cellvars
        self.co_filename = co_filename
        self.co_name = co_name
        self.co_firstlineno = co_firstlineno
        self.co_lnotab = co_lnotab


class DecodeInstruction(object):
    __slots__ = (
        "custom_op",
        "arg1",
        "arg2",
        "start_op",
        "start_arg",
        "alias_op",
        "alias_arg",
        "post_op",
        "post_arg",
    )

    def __init__(self, custom_op, arg1, arg2, start_op, start_arg, alias_op, alias_arg, post_op, post_arg):
        self.custom_op = custom_op
        self.arg1 = arg1
        self.arg2 = arg2
        self.start_op = start_op
        self.start_arg = start_arg
        self.alias_op = alias_op
        self.alias_arg = alias_arg
        self.post_op = post_op
        self.post_arg = post_arg


class StdInstruction(object):
    __slots__ = ("op", "raw_arg", "target_index", "size", "arg")

    def __init__(self, op, raw_arg, target_index):
        self.op = op
        self.raw_arg = raw_arg
        self.target_index = target_index
        self.size = 2
        self.arg = 0


def _ensure_py36_runtime():
    if sys.version_info[:2] != (3, 6):
        raise SystemExit(
            "convert-file / convert-dir 需要在 Python 3.6 下运行。\n"
            "当前解释器: {}.{}.{}\n"
            "建议使用: python3.6 tools/gunfire_pyc_convert.py ...".format(
                sys.version_info[0],
                sys.version_info[1],
                sys.version_info[2],
            )
        )


class MarshalReader(object):
    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.refs = []

    def _read(self, n):
        end = self.pos + n
        if end > len(self.data):
            raise EOFError("marshal EOF at {} need {}".format(self.pos, n))
        out = self.data[self.pos:end]
        self.pos = end
        return out

    def _read_byte(self):
        if self.pos >= len(self.data):
            raise EOFError("marshal EOF at {}".format(self.pos))
        out = self.data[self.pos]
        self.pos += 1
        if isinstance(out, int):
            return out
        return ord(out)

    def _read_int32(self):
        return struct.unpack("<i", self._read(4))[0]

    def _read_int64(self):
        return struct.unpack("<q", self._read(8))[0]

    def _reserve_ref(self, flag_ref):
        if not flag_ref:
            return None
        idx = len(self.refs)
        self.refs.append(None)
        return idx

    def _store_ref(self, idx, obj):
        if idx is not None:
            self.refs[idx] = obj
        return obj

    def read_object(self):
        tc = self._read_byte()
        flag_ref = (tc & FLAG_REF) != 0
        t = chr(tc & 0x7F)

        if t == TYPE_REF:
            idx = self._read_int32()
            if idx < 0 or idx >= len(self.refs):
                raise ValueError("bad TYPE_REF index {} (refs={})".format(idx, len(self.refs)))
            return self.refs[idx]
        if t == TYPE_NULL:
            return NULL_SENTINEL
        if t == TYPE_NONE:
            return self._store_ref(self._reserve_ref(flag_ref), None)
        if t == TYPE_FALSE:
            return self._store_ref(self._reserve_ref(flag_ref), False)
        if t == TYPE_TRUE:
            return self._store_ref(self._reserve_ref(flag_ref), True)
        if t == TYPE_STOPITER:
            return self._store_ref(self._reserve_ref(flag_ref), StopIteration)
        if t == TYPE_ELLIPSIS:
            return self._store_ref(self._reserve_ref(flag_ref), Ellipsis)
        if t == TYPE_INT:
            return self._store_ref(self._reserve_ref(flag_ref), self._read_int32())
        if t == TYPE_INT64:
            return self._store_ref(self._reserve_ref(flag_ref), self._read_int64())
        if t == TYPE_LONG:
            n = self._read_int32()
            sign = 1
            if n < 0:
                sign = -1
                n = -n
            x = 0
            shift = 0
            for _ in range(n):
                d = struct.unpack("<H", self._read(2))[0]
                x |= int(d) << shift
                shift += 15
            return self._store_ref(self._reserve_ref(flag_ref), sign * x)
        if t == TYPE_FLOAT:
            n = self._read_byte()
            s = self._read(n).decode("ascii")
            return self._store_ref(self._reserve_ref(flag_ref), float(s))
        if t == TYPE_BINARY_FLOAT:
            return self._store_ref(self._reserve_ref(flag_ref), struct.unpack("<d", self._read(8))[0])
        if t == TYPE_COMPLEX:
            n1 = self._read_byte()
            s1 = self._read(n1).decode("ascii")
            n2 = self._read_byte()
            s2 = self._read(n2).decode("ascii")
            return self._store_ref(self._reserve_ref(flag_ref), complex(float(s1), float(s2)))
        if t == TYPE_BINARY_COMPLEX:
            re = struct.unpack("<d", self._read(8))[0]
            im = struct.unpack("<d", self._read(8))[0]
            return self._store_ref(self._reserve_ref(flag_ref), complex(re, im))
        if t == TYPE_STRING:
            n = self._read_int32()
            if n < 0:
                raise ValueError("negative TYPE_STRING size {}".format(n))
            return self._store_ref(self._reserve_ref(flag_ref), self._read(n))
        if t in (TYPE_INTERNED, TYPE_ASCII, TYPE_ASCII_INTERNED, TYPE_SHORT_ASCII, TYPE_SHORT_ASCII_INTERNED, TYPE_UNICODE):
            if t in (TYPE_SHORT_ASCII, TYPE_SHORT_ASCII_INTERNED):
                n = self._read_byte()
            else:
                n = self._read_int32()
            if n < 0:
                raise ValueError("negative unicode size {}".format(n))
            raw = self._read(n)
            try:
                s = raw.decode("utf-8", "surrogatepass")
            except TypeError:
                s = raw.decode("utf-8")
            return self._store_ref(self._reserve_ref(flag_ref), s)
        if t == TYPE_SMALL_TUPLE:
            n = self._read_byte()
            idx = self._reserve_ref(flag_ref)
            items = []
            if idx is not None:
                self.refs[idx] = items
            for _ in range(n):
                items.append(self.read_object())
            return self._store_ref(idx, tuple(items))
        if t == TYPE_TUPLE:
            n = self._read_int32()
            if n < 0:
                raise ValueError("negative tuple size {}".format(n))
            idx = self._reserve_ref(flag_ref)
            items = []
            if idx is not None:
                self.refs[idx] = items
            for _ in range(n):
                items.append(self.read_object())
            return self._store_ref(idx, tuple(items))
        if t == TYPE_LIST:
            n = self._read_int32()
            if n < 0:
                raise ValueError("negative list size {}".format(n))
            idx = self._reserve_ref(flag_ref)
            out = []
            if idx is not None:
                self.refs[idx] = out
            for _ in range(n):
                out.append(self.read_object())
            return out
        if t == TYPE_SET:
            n = self._read_int32()
            if n < 0:
                raise ValueError("negative set size {}".format(n))
            idx = self._reserve_ref(flag_ref)
            out = set()
            if idx is not None:
                self.refs[idx] = out
            for _ in range(n):
                out.add(self.read_object())
            return out
        if t == TYPE_FROZENSET:
            n = self._read_int32()
            if n < 0:
                raise ValueError("negative frozenset size {}".format(n))
            idx = self._reserve_ref(flag_ref)
            items = []
            if idx is not None:
                self.refs[idx] = items
            for _ in range(n):
                items.append(self.read_object())
            return self._store_ref(idx, frozenset(items))
        if t == TYPE_DICT:
            idx = self._reserve_ref(flag_ref)
            out = {}
            if idx is not None:
                self.refs[idx] = out
            while True:
                k = self.read_object()
                if k is NULL_SENTINEL:
                    break
                v = self.read_object()
                out[k] = v
            return out
        if t == TYPE_CODE:
            idx = self._reserve_ref(flag_ref)

            # Verified from sub_180103420 (r_object):
            # argcount, kwonlyargcount, nlocals, stacksize, flags, custom_split
            # + 8 objects
            # + firstlineno + lnotab
            argcount = self._read_int32()
            kwonlyargcount = self._read_int32()
            nlocals = self._read_int32()
            stacksize = self._read_int32()
            flags = self._read_int32()
            custom_split = self._read_int32()

            co_code = self.read_object()
            co_consts = self.read_object()
            co_names = self.read_object()
            co_varnames = self.read_object()
            co_freevars = self.read_object()
            co_cellvars = self.read_object()
            co_filename = self.read_object()
            co_name = self.read_object()
            firstlineno = self._read_int32()
            lnotab = self.read_object()

            cc = CustomCode(
                argcount,
                kwonlyargcount,
                nlocals,
                stacksize,
                flags,
                custom_split,
                co_code,
                co_consts,
                co_names,
                co_varnames,
                co_freevars,
                co_cellvars,
                co_filename,
                co_name,
                firstlineno,
                lnotab,
            )
            return self._store_ref(idx, cc)

        raise ValueError("unsupported marshal type '{}' at {}".format(t, self.pos - 1))


def load_custom_pyc(path):
    data = open(path, "rb").read()
    if len(data) < 12:
        raise ValueError("pyc too short: {}".format(path))
    header = data[:12]
    reader = MarshalReader(data[12:])
    root = reader.read_object()
    return header, root


def load_std_pyc(path):
    data = open(path, "rb").read()
    if len(data) < 12:
        raise ValueError("std pyc too short: {}".format(path))
    return marshal.loads(data[12:])


def decode_custom_stream(code_bytes, split):
    if not isinstance(code_bytes, (bytes, bytearray)):
        raise TypeError("co_code is not bytes")
    if split < 0 or split > len(code_bytes):
        raise ValueError("bad split {} for code len {}".format(split, len(code_bytes)))

    op_stream = code_bytes[:split]
    arg_stream = code_bytes[split:]

    op_i = 0
    arg_i = 0
    ext_carry = 0
    out = []

    while op_i < len(op_stream):
        start_op = op_i
        start_arg = arg_i
        alias_op = None
        alias_arg = None

        if arg_i >= len(arg_stream):
            # Observed in samples: a trailing opcode byte can remain after arg stream is exhausted.
            # The eval loop cannot fetch it (missing paired arg), so we stop here.
            break

        n219 = op_stream[op_i]
        op_i += 1
        n3_6 = arg_stream[arg_i]
        arg_i += 1
        n3_8 = ext_carry

        while True:
            if n219 == MARKER_OPCODE:
                if arg_i >= len(arg_stream):
                    raise ValueError("marker missing extension byte at arg {}".format(arg_i))

                # n3_8 = *(arg_ptr) | (n3_8 << 8)
                n3_8 = (arg_stream[arg_i] | ((n3_8 & 0xFFFFFFFF) << 8)) & 0xFFFFFFFF
                ext_carry = n3_8
                v57 = (n3_6 & 0xFFFFFFFF) << 8

                if op_i >= len(op_stream):
                    raise ValueError("marker missing fused opcode at op {}".format(op_i))
                next_op = op_stream[op_i]
                next_op_index = op_i

                if next_op in MARKER_SPECIAL_NEXT:
                    op_i += 1
                    if arg_i + 2 >= len(arg_stream):
                        raise ValueError("marker special missing args at arg {}".format(arg_i))
                    # alt entry can jump directly to fused opcode/arg1 coordinates.
                    alias_op = next_op_index
                    alias_arg = arg_i + 1
                    n3_6 = (arg_stream[arg_i + 1] | v57) & 0xFFFFFFFF
                    n3_22 = (arg_stream[arg_i + 2] | ((n3_8 & 0xFFFFFFFF) << 8)) & 0xFFFFFFFF
                    arg_i += 3
                    ext_carry = 0
                    out.append(
                        DecodeInstruction(next_op, n3_6, n3_22, start_op, start_arg, alias_op, alias_arg, op_i, arg_i)
                    )
                    break

                op_i += 1
                if arg_i + 1 >= len(arg_stream):
                    raise ValueError("marker default missing args at arg {}".format(arg_i))
                alias_op = next_op_index
                alias_arg = arg_i + 1
                # default: n3_6 = arg_ptr[1] | (old_arg << 8), arg_ptr += 2, n219 = next_op
                n3_6 = (arg_stream[arg_i + 1] | v57) & 0xFFFFFFFF
                arg_i += 2
                n219 = next_op
                continue

            n3_22 = None
            if n219 in DUAL_ARG_OPS:
                if arg_i >= len(arg_stream):
                    raise ValueError("dual opcode {} missing arg2".format(n219))
                n3_22 = arg_stream[arg_i]
                arg_i += 1

            out.append(DecodeInstruction(n219, n3_6, n3_22, start_op, start_arg, alias_op, alias_arg, op_i, arg_i))

            # evalframe fastpath inside case 253:
            # if next opcode is 0xC5 / 0xF0, it consumes that opcode + 2 arg bytes
            # and executes it immediately.
            # We still emit two logical instructions (COMPARE_OP + jump) for conversion,
            # but must consume the same raw bytes to stay synchronized with streams.
            if n219 == 253 and op_i < len(op_stream):
                fast_next = op_stream[op_i]
                if fast_next in (197, 240):
                    if arg_i + 1 >= len(arg_stream):
                        raise ValueError("compare fastpath missing jump args at arg {}".format(arg_i))
                    j_start_op = op_i
                    j_start_arg = arg_i
                    op_i += 1
                    j_arg1 = arg_stream[arg_i]
                    j_arg2 = arg_stream[arg_i + 1]
                    arg_i += 2
                    out.append(DecodeInstruction(fast_next, j_arg1, j_arg2, j_start_op, j_start_arg, None, None, op_i, arg_i))
            break

    return out, len(op_stream), len(arg_stream), op_i, arg_i


def decode_std_wordcode(code_bytes):
    out = []
    i = 0
    ext = 0
    n = len(code_bytes)
    while i < n:
        op = code_bytes[i]
        arg = code_bytes[i + 1] if i + 1 < n else 0
        if not isinstance(op, int):
            op = ord(op)
            arg = ord(code_bytes[i + 1]) if i + 1 < n else 0
        full = (arg | (ext << 8)) & 0xFFFFFFFF
        if op == EXTENDED_ARG:
            ext = full
            i += 2
            continue
        out.append((op, full, i))
        ext = 0
        i += 2
    return out


def iter_custom_code_objects(obj):
    if isinstance(obj, CustomCode):
        yield obj
        for c in obj.co_consts:
            for x in iter_custom_code_objects(c):
                yield x
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for it in obj:
            for x in iter_custom_code_objects(it):
                yield x
    elif isinstance(obj, dict):
        for k, v in obj.items():
            for x in iter_custom_code_objects(k):
                yield x
            for x in iter_custom_code_objects(v):
                yield x


def iter_std_code_objects(obj):
    if isinstance(obj, types.CodeType):
        yield obj
        for c in obj.co_consts:
            for x in iter_std_code_objects(c):
                yield x
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for it in obj:
            for x in iter_std_code_objects(it):
                yield x
    elif isinstance(obj, dict):
        for k, v in obj.items():
            for x in iter_std_code_objects(k):
                yield x
            for x in iter_std_code_objects(v):
                yield x


def derive_opcode_map(custom_dir, std_dir, quiet=False):
    pairs = []
    for name in sorted(os.listdir(custom_dir)):
        if not name.endswith(".pyc"):
            continue
        cpath = os.path.join(custom_dir, name)
        spath = os.path.join(std_dir, name)
        if not os.path.isfile(spath):
            continue
        pairs.append((cpath, spath))

    edge_counter = collections.Counter()
    custom_counter = collections.Counter()
    bad_pairs = 0
    total_code_pairs = 0
    matched_code_pairs = 0
    seen_custom_ops = set()

    for cpath, spath in pairs:
        try:
            _, croot = load_custom_pyc(cpath)
            sroot = load_std_pyc(spath)
        except Exception:
            bad_pairs += 1
            continue

        c_codes = list(iter_custom_code_objects(croot))
        s_codes = list(iter_std_code_objects(sroot))
        pair_count = min(len(c_codes), len(s_codes))
        total_code_pairs += pair_count

        for i in range(pair_count):
            cc = c_codes[i]
            sc = s_codes[i]
            try:
                cins, _, _, _, _ = decode_custom_stream(cc.co_code, cc.co_custom_split)
                sins = decode_std_wordcode(sc.co_code)
            except Exception:
                continue

            for inst in cins:
                seen_custom_ops.add(inst.custom_op)
                custom_counter[inst.custom_op] += 1

            if len(cins) != len(sins):
                continue

            matched_code_pairs += 1
            for j in range(len(cins)):
                cop = cins[j].custom_op
                sop = sins[j][0]
                edge_counter[(cop, sop)] += 1

    mapping = {}
    confidence = {}
    for cop in sorted(seen_custom_ops):
        edges = [(k[1], v) for (k, v) in edge_counter.items() if k[0] == cop]
        if not edges:
            continue
        edges.sort(key=lambda x: x[1], reverse=True)
        best_sop, best_n = edges[0]
        mapping[cop] = best_sop
        total = sum(v for _, v in edges)
        confidence[cop] = (best_n, total)

    # Hard confirmations from IDA:
    mapping[24] = 10     # UNARY_POSITIVE
    mapping[113] = 152   # BUILD_TUPLE_UNPACK
    mapping[118] = 144   # marker/ext semantics

    if not quiet:
        print("[map] files={} bad_files={}".format(len(pairs), bad_pairs))
        print("[map] code_pairs_total={} matched_len={}".format(total_code_pairs, matched_code_pairs))
        unresolved = sorted(seen_custom_ops - set(mapping.keys()))
        print("[map] seen_custom_ops={} mapped={} unresolved={}".format(len(seen_custom_ops), len(mapping), len(unresolved)))
        if unresolved:
            print("[map] unresolved custom ops: {}".format(unresolved))
        low_conf = []
        for cop in sorted(confidence):
            best, total = confidence[cop]
            if total > 0 and best * 100 < total * 70:
                low_conf.append((cop, best, total, mapping.get(cop)))
        if low_conf:
            print("[map] low confidence entries (<70%):")
            for cop, best, total, sop in low_conf[:30]:
                print("  custom {:3d} -> std {:3d}   {}/{}".format(cop, sop, best, total))

    return mapping


def _s8(x):
    v = int(x) & 0xFF
    return v - 256 if (v & 0x80) else v


def _normalize_header_to_std36(header12):
    if not isinstance(header12, (bytes, bytearray)) or len(header12) < 12:
        raise ValueError("bad pyc header length: {}".format(len(header12) if header12 is not None else None))
    return bytes(MAGIC36[:4]) + bytes(header12[4:12])


def _required_code_units(op, arg):
    if op < HAVE_ARGUMENT:
        return 1
    units = 1
    value = int(arg) >> 8
    while value > 0:
        units += 1
        value >>= 8
    return units


def _emit_wordcode(op, arg, total_units, out):
    if op < HAVE_ARGUMENT:
        out.extend(bytearray([op & 0xFF, 0]))
        return

    if arg < 0:
        raise ValueError("negative oparg for opcode {}: {}".format(op, arg))

    min_units = _required_code_units(op, arg)
    extra_zero_ext = max(0, int(total_units) - int(min_units))
    for _ in range(extra_zero_ext):
        out.extend(bytearray([EXTENDED_ARG, 0]))

    parts = []
    value = int(arg) >> 8
    while value > 0:
        parts.append(value & 0xFF)
        value >>= 8
    for b in reversed(parts):
        out.extend(bytearray([EXTENDED_ARG, b & 0xFF]))
    out.extend(bytearray([op & 0xFF, int(arg) & 0xFF]))


def _as_tuple(x):
    if isinstance(x, tuple):
        return x
    if isinstance(x, list):
        return tuple(x)
    return tuple(x)


def convert_code_object(cc, opcode_map):
    if not isinstance(cc, CustomCode):
        return cc

    ins, op_len, arg_len, used_op, used_arg = decode_custom_stream(cc.co_code, cc.co_custom_split)
    if used_arg != arg_len:
        raise ValueError(
            "decode arg stream not fully consumed for {}: op {}/{} arg {}/{}".format(
                cc.co_name, used_op, op_len, used_arg, arg_len
            )
        )

    coord_to_idx = {}
    for i, it in enumerate(ins):
        coord_to_idx[(it.start_op, it.start_arg)] = i
        if it.alias_op is not None and it.alias_arg is not None:
            coord_to_idx[(it.alias_op, it.alias_arg)] = i

    std_ins = []
    for i, it in enumerate(ins):
        if it.custom_op not in opcode_map:
            raise KeyError("unmapped custom opcode {} in {}".format(it.custom_op, cc.co_name))
        std_op = int(opcode_map[it.custom_op])

        target_index = None
        raw_arg = it.arg1 if it.arg1 is not None else 0

        if it.custom_op in DUAL_ABS_OPS:
            if it.arg2 is None:
                raise ValueError("dual abs opcode {} missing arg2".format(it.custom_op))
            tgt = (int(it.arg1), int(it.arg2))
            if tgt not in coord_to_idx:
                raise KeyError("abs jump target {} not found in {} ({})".format(tgt, cc.co_name, i))
            target_index = coord_to_idx[tgt]
            raw_arg = 0
        elif it.custom_op in DUAL_REL_OPS:
            if it.arg2 is None:
                raise ValueError("dual rel opcode {} missing arg2".format(it.custom_op))

            # Evalframe uses zero-extended opcode/arg bytes here, so dual-relative
            # control flow is based on unsigned stream-coordinate deltas.
            tgt_u8 = (int(it.post_op + it.arg1), int(it.post_arg + it.arg2))
            if tgt_u8 not in coord_to_idx:
                raise KeyError("rel jump target not found in {} ({}): u8={}".format(cc.co_name, i, tgt_u8))
            target_index = coord_to_idx[tgt_u8]
            raw_arg = 0

        std_ins.append(StdInstruction(std_op, int(raw_arg), target_index))

    # 迭代求解每条指令的最终偏移。jump 参数变化后，EXTENDED_ARG 数量也可能随之变化。
    for _ in range(64):
        changed = False
        offsets = [0] * len(std_ins)
        cur = 0
        for i, s in enumerate(std_ins):
            offsets[i] = cur
            cur += s.size

        for i, s in enumerate(std_ins):
            if s.target_index is not None:
                if s.target_index < 0 or s.target_index >= len(std_ins):
                    raise IndexError("bad target index {} at {}".format(s.target_index, i))
                tgt_off = offsets[s.target_index]
                if s.op in STD_HAS_JABS:
                    s.arg = tgt_off
                elif s.op in STD_HAS_JREL:
                    s.arg = tgt_off - (offsets[i] + s.size)
                else:
                    raise ValueError(
                        "opcode {} has coord target but is not jump in std set ({}:{})".format(
                            s.op, cc.co_name, i
                        )
                    )
            else:
                s.arg = s.raw_arg

            required_units = _required_code_units(s.op, s.arg)
            new_size = 2 * required_units
            if new_size != s.size:
                s.size = new_size
                changed = True
        if not changed:
            break
    else:
        raise RuntimeError("offset solver did not converge for {}".format(cc.co_name))

    out_code = bytearray()
    for s in std_ins:
        _emit_wordcode(s.op, s.arg, s.size // 2, out_code)
    new_consts = []
    for c in cc.co_consts:
        if isinstance(c, CustomCode):
            new_consts.append(convert_code_object(c, opcode_map))
        else:
            new_consts.append(c)
    out_lnotab = cc.co_lnotab if isinstance(cc.co_lnotab, (bytes, bytearray)) else bytes(cc.co_lnotab)

    new_code = types.CodeType(
        int(cc.co_argcount),
        int(cc.co_kwonlyargcount),
        int(cc.co_nlocals),
        int(cc.co_stacksize),
        int(cc.co_flags),
        bytes(out_code),
        tuple(new_consts),
        _as_tuple(cc.co_names),
        _as_tuple(cc.co_varnames),
        cc.co_filename,
        cc.co_name,
        int(cc.co_firstlineno),
        out_lnotab,
        _as_tuple(cc.co_freevars),
        _as_tuple(cc.co_cellvars),
    )
    return new_code


def convert_one_file(in_pyc, out_pyc, opcode_map):
    header, root = load_custom_pyc(in_pyc)
    if not isinstance(root, CustomCode):
        raise TypeError("root object is not CustomCode: {}".format(type(root)))
    new_root = convert_code_object(root, opcode_map)
    out_data = _normalize_header_to_std36(header) + marshal.dumps(new_root)
    out_dir = os.path.dirname(out_pyc)
    if out_dir:
        try:
            os.makedirs(out_dir)
        except OSError:
            if not os.path.isdir(out_dir):
                raise
    with open(out_pyc, "wb") as f:
        f.write(out_data)


def load_opcode_map(path):
    with open(path, "r") as f:
        raw = json.load(f)
    out = {}
    for k, v in raw.items():
        out[int(k)] = int(v)
    return out


def save_opcode_map(path, mapping):
    data = {str(int(k)): int(v) for k, v in sorted(mapping.items())}
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def cmd_derive_map(args):
    m = derive_opcode_map(args.custom_dir, args.std_dir, quiet=False)
    if args.out_json:
        save_opcode_map(args.out_json, m)
        print("[ok] map saved:", args.out_json)
    else:
        print(json.dumps({str(k): v for k, v in sorted(m.items())}, indent=2, sort_keys=True))


def _iter_pyc_files(base_dir):
    out = []
    for root, _, files in os.walk(base_dir):
        for n in files:
            if n.endswith(".pyc"):
                out.append(os.path.join(root, n))
    out.sort()
    return out


def _resolve_map(args):
    if args.map_json:
        return load_opcode_map(args.map_json)
    if args.auto_custom_dir and args.auto_std_dir:
        print("[map] deriving opcode map from", args.auto_custom_dir, "vs", args.auto_std_dir)
        return derive_opcode_map(args.auto_custom_dir, args.auto_std_dir, quiet=False)
    raise ValueError("need --map-json OR (--auto-custom-dir + --auto-std-dir)")


def cmd_convert_file(args):
    _ensure_py36_runtime()
    m = _resolve_map(args)
    convert_one_file(args.in_pyc, args.out_pyc, m)
    print("[ok] converted:", args.out_pyc)


def _co_filename_to_relpath(co_filename):
    if not co_filename:
        return None

    parts = []
    for part in str(co_filename).replace("\\", "/").split("/"):
        if not part or part in (".", "..") or part.endswith(":"):
            continue
        parts.append(part)

    if not parts:
        return None

    relpath = Path(*parts)
    if relpath.suffix == ".py":
        return str(relpath.with_suffix(".pyc"))
    if relpath.suffix == ".pyc":
        return str(relpath)
    return "{}.pyc".format(relpath)


def _extract_co_filename(in_pyc):
    _, root = load_custom_pyc(in_pyc)
    if isinstance(root, CustomCode):
        return root.co_filename
    return None


def _build_output_tasks(in_files, in_dir, out_dir, real_names):
    tasks = []
    duplicate_counts = {}
    fallback_count = 0

    in_dir = Path(in_dir)
    out_dir = Path(out_dir)

    for in_pyc in in_files:
        relative_output = None
        if real_names:
            try:
                relative_output = _co_filename_to_relpath(_extract_co_filename(in_pyc))
            except Exception:
                relative_output = None

        if relative_output:
            duplicate_index = duplicate_counts.get(relative_output, 0)
            duplicate_counts[relative_output] = duplicate_index + 1
            if duplicate_index:
                path = Path(relative_output)
                relative_output = str(
                    path.with_name("{}__dup{}{}".format(path.stem, duplicate_index, path.suffix))
                )
        else:
            fallback_count += 1
            relative_output = str(Path(in_pyc).relative_to(in_dir))

        tasks.append((str(in_pyc), str(out_dir / relative_output)))

    if real_names and fallback_count:
        print("[warn] {} files had no co_filename, using original relative path".format(fallback_count))
    return tasks


def cmd_list_names(args):
    in_dir = Path(args.in_dir)
    in_files = _iter_pyc_files(args.in_dir)
    if args.limit and args.limit > 0:
        in_files = in_files[: args.limit]

    for in_pyc in in_files:
        try:
            rel_in = Path(in_pyc).relative_to(in_dir)
            rel_out = _co_filename_to_relpath(_extract_co_filename(in_pyc)) or "<none>"
        except Exception:
            rel_in = Path(in_pyc).relative_to(in_dir)
            rel_out = "<error>"
        print("{}\t{}".format(rel_in, rel_out))

    print("[list] total={} files".format(len(in_files)))


def cmd_convert_dir(args):
    _ensure_py36_runtime()
    m = _resolve_map(args)
    in_files = _iter_pyc_files(args.in_dir)
    if args.limit and args.limit > 0:
        in_files = in_files[: args.limit]
    total = len(in_files)
    jobs = int(args.jobs) if args.jobs and args.jobs > 0 else 1
    progress_every = int(args.progress_every) if args.progress_every and args.progress_every > 0 else 200
    tasks = _build_output_tasks(
        in_files=in_files,
        in_dir=args.in_dir,
        out_dir=args.out_dir,
        real_names=getattr(args, "real_names", False),
    )

    if getattr(args, "list_only", False):
        for in_pyc, out_pyc in tasks:
            print("{} -> {}".format(in_pyc, out_pyc))
        print("[list] total={} files".format(total))
        return

    ok = 0
    fail = 0

    def _convert_one_task(task):
        in_pyc, out_pyc = task
        try:
            convert_one_file(in_pyc, out_pyc, m)
            return True, in_pyc, out_pyc, ""
        except Exception as e:
            return False, in_pyc, out_pyc, str(e)

    if jobs == 1:
        result_iter = (_convert_one_task(task) for task in tasks)
        for idx, result in enumerate(result_iter, 1):
            ok_one, in_pyc, out_pyc, err = result
            if ok_one:
                ok += 1
            else:
                fail += 1
                print("[fail] {} -> {} : {}".format(in_pyc, out_pyc, err))
            if idx % progress_every == 0 or idx == total:
                print("[progress] {}/{} ok={} fail={}".format(idx, total, ok, fail))
    else:
        print("[info] convert-dir parallel jobs={}".format(jobs))
        with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
            for idx, result in enumerate(pool.map(_convert_one_task, tasks), 1):
                ok_one, in_pyc, out_pyc, err = result
                if ok_one:
                    ok += 1
                else:
                    fail += 1
                    print("[fail] {} -> {} : {}".format(in_pyc, out_pyc, err))
                if idx % progress_every == 0 or idx == total:
                    print("[progress] {}/{} ok={} fail={}".format(idx, total, ok, fail))

    print("[done] total={} ok={} fail={}".format(total, ok, fail))
    if fail:
        raise SystemExit(2)


def build_arg_parser():
    p = argparse.ArgumentParser(
        description="Gunfire custom pyc -> standard pyc (Python 3.6)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "推荐流程:\n"
            "  1. 先用 fls_unpacker_improved.py 解出 pyc\n"
            "  2. 再用本脚本 + opcode_map.json 还原 opcode\n"
            "  3. 建议 convert-dir 时带上 --real-names，输出目录更接近源码结构"
        ),
    )
    sp = p.add_subparsers(dest="cmd")
    sp.required = True

    p_map = sp.add_parser("derive-map", help="derive custom->std opcode map from paired pyc dirs")
    p_map.add_argument("--custom-dir", required=True, help="dir with custom pyc (e.g. extracted_data2)")
    p_map.add_argument("--std-dir", required=True, help="dir with paired std pyc (e.g. .tmp_std_compile)")
    p_map.add_argument("--out-json", help="save map json")
    p_map.set_defaults(func=cmd_derive_map)

    p_cf = sp.add_parser("convert-file", help="convert one custom pyc to std pyc")
    p_cf.add_argument("--in-pyc", required=True)
    p_cf.add_argument("--out-pyc", required=True)
    p_cf.add_argument("--map-json", help="opcode map json")
    p_cf.add_argument("--auto-custom-dir", help="derive map automatically from this custom dir")
    p_cf.add_argument("--auto-std-dir", help="derive map automatically from this std dir")
    p_cf.set_defaults(func=cmd_convert_file)

    p_cd = sp.add_parser("convert-dir", help="convert all pyc under a directory")
    p_cd.add_argument("--in-dir", required=True)
    p_cd.add_argument("--out-dir", required=True)
    p_cd.add_argument("--map-json", help="opcode map json")
    p_cd.add_argument("--auto-custom-dir", help="derive map automatically from this custom dir")
    p_cd.add_argument("--auto-std-dir", help="derive map automatically from this std dir")
    p_cd.add_argument("--jobs", type=int, default=1, help="parallel workers for conversion (default 1)")
    p_cd.add_argument("--progress-every", type=int, default=200, help="progress print interval (default 200)")
    p_cd.add_argument("--limit", type=int, default=0, help="only convert first N pyc files (debug)")
    p_cd.add_argument("--real-names", action="store_true", help="organize output by real co_filename paths")
    p_cd.add_argument("--list-only", action="store_true", help="only list input->output mapping")
    p_cd.set_defaults(func=cmd_convert_dir)

    p_ln = sp.add_parser("list-names", help="list co_filename mapping for all pyc in a directory")
    p_ln.add_argument("--in-dir", required=True)
    p_ln.add_argument("--limit", type=int, default=0)
    p_ln.set_defaults(func=cmd_list_names)
    return p


def main():
    parser = build_arg_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
