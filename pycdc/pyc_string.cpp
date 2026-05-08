#include "pyc_string.h"
#include "pyc_module.h"
#include "data.h"
#include <stdexcept>

static bool check_ascii(const std::string& data)
{
    auto cp = reinterpret_cast<const unsigned char*>(data.c_str());
    while (*cp) {
        if (*cp & 0x80)
            return false;
        ++cp;
    }
    return true;
}

static bool decode_utf8_codepoint(const std::string& data, size_t pos,
                                  size_t& advance, unsigned int& codepoint)
{
    const unsigned char* bytes = reinterpret_cast<const unsigned char*>(data.data());
    const size_t size = data.size();
    unsigned char lead = bytes[pos];

    if (lead < 0x80) {
        advance = 1;
        codepoint = lead;
        return true;
    }

    size_t need = 0;
    unsigned int value = 0;
    unsigned int min_value = 0;
    if ((lead & 0xE0) == 0xC0) {
        need = 2;
        value = lead & 0x1F;
        min_value = 0x80;
    } else if ((lead & 0xF0) == 0xE0) {
        need = 3;
        value = lead & 0x0F;
        min_value = 0x800;
    } else if ((lead & 0xF8) == 0xF0) {
        need = 4;
        value = lead & 0x07;
        min_value = 0x10000;
    } else {
        return false;
    }

    if (pos + need > size)
        return false;

    for (size_t i = 1; i < need; ++i) {
        unsigned char ch = bytes[pos + i];
        if ((ch & 0xC0) != 0x80)
            return false;
        value = (value << 6) | (ch & 0x3F);
    }

    if (value < min_value || value > 0x10FFFF)
        return false;

    advance = need;
    codepoint = value;
    return true;
}

/* PycString */
void PycString::load(PycData* stream, PycModule* mod)
{
    if (type() == TYPE_STRINGREF) {
        PycRef<PycString> str = mod->getIntern(stream->get32());
        m_type = str->m_type;
        m_value = str->m_value;
    } else {
        int length;
        if (type() == TYPE_SHORT_ASCII || type() == TYPE_SHORT_ASCII_INTERNED)
            length = stream->getByte();
        else
            length = stream->get32();

        if (length < 0)
            throw std::bad_alloc();

        m_value.resize(length);
        if (length) {
            stream->getBuffer(length, &m_value.front());
            if (type() == TYPE_ASCII || type() == TYPE_ASCII_INTERNED ||
                    type() == TYPE_SHORT_ASCII || type() == TYPE_SHORT_ASCII_INTERNED) {
                if (!check_ascii(m_value))
                    throw std::runtime_error("Invalid bytes in ASCII string");
            }
        }

        if (type() == TYPE_INTERNED || type() == TYPE_ASCII_INTERNED ||
                type() == TYPE_SHORT_ASCII_INTERNED)
            mod->intern(this);
    }
}

bool PycString::isEqual(PycRef<PycObject> obj) const
{
    if (type() != obj.type())
        return false;

    PycRef<PycString> strObj = obj.cast<PycString>();
    return isEqual(strObj->m_value);
}

void PycString::print(std::ostream &pyc_output, PycModule* mod, bool triple,
                      const char* parent_f_string_quote)
{
    char prefix = 0;
    switch (type()) {
    case TYPE_STRING:
        prefix = mod->strIsUnicode() ? 'b' : 0;
        break;
    case PycObject::TYPE_UNICODE:
        prefix = mod->strIsUnicode() ? 0 : 'u';
        break;
    case PycObject::TYPE_INTERNED:
        prefix = mod->internIsBytes() ? 'b' : 0;
        break;
    case PycObject::TYPE_ASCII:
    case PycObject::TYPE_ASCII_INTERNED:
    case PycObject::TYPE_SHORT_ASCII:
    case PycObject::TYPE_SHORT_ASCII_INTERNED:
        // These types don't exist until Python 3.4
        prefix = 0;
        break;
    default:
        throw std::runtime_error("Invalid string type");
    }

    if (prefix != 0)
        pyc_output << prefix;

    if (m_value.empty()) {
        pyc_output << "''";
        return;
    }

    // Determine preferred quote style (Emulate Python's method)
    bool useQuotes = false;
    if (!parent_f_string_quote) {
        for (char ch : m_value) {
            if (ch == '\'') {
                useQuotes = true;
            } else if (ch == '"') {
                useQuotes = false;
                break;
            }
        }
    } else {
        useQuotes = parent_f_string_quote[0] == '"';
    }

    // Output the string
    if (!parent_f_string_quote) {
        if (triple)
            pyc_output << (useQuotes ? R"(""")" : "'''");
        else
            pyc_output << (useQuotes ? '"' : '\'');
    }
    for (size_t i = 0; i < m_value.size(); ++i) {
        unsigned char uch = static_cast<unsigned char>(m_value[i]);
        char ch = static_cast<char>(uch);
        if (static_cast<unsigned char>(ch) < 0x20 || ch == 0x7F) {
            if (ch == '\r') {
                pyc_output << "\\r";
            } else if (ch == '\n') {
                if (triple)
                    pyc_output << '\n';
                else
                    pyc_output << "\\n";
            } else if (ch == '\t') {
                pyc_output << "\\t";
            } else {
                formatted_print(pyc_output, "\\x%02x", (ch & 0xFF));
            }
        } else if (uch >= 0x80) {
            if (type() == TYPE_UNICODE) {
                size_t advance = 0;
                unsigned int codepoint = 0;
                if (decode_utf8_codepoint(m_value, i, advance, codepoint)) {
                    if (codepoint >= 0xD800 && codepoint <= 0xDFFF) {
                        formatted_print(pyc_output, "\\u%04x", codepoint);
                    } else {
                        pyc_output.write(m_value.data() + i, advance);
                    }
                    i += advance - 1;
                } else {
                    formatted_print(pyc_output, "\\x%02x", uch);
                }
            } else {
                formatted_print(pyc_output, "\\x%02x", (ch & 0xFF));
            }
        } else {
            if (!useQuotes && ch == '\'')
                pyc_output << R"(\')";
            else if (useQuotes && ch == '"')
                pyc_output << R"(\")";
            else if (ch == '\\')
                pyc_output << R"(\\)";
            else if (parent_f_string_quote && ch == '{')
                pyc_output << "{{";
            else if (parent_f_string_quote && ch == '}')
                pyc_output << "}}";
            else
                pyc_output << ch;
        }
    }
    if (!parent_f_string_quote) {
        if (triple)
            pyc_output << (useQuotes ? R"(""")" : "'''");
        else
            pyc_output << (useQuotes ? '"' : '\'');
    }
}
