#!/usr/bin/env python3
"""用 unicorn 模拟 m1logic4.dll 里的资源文件名 hash 函数 sub_18020F760。

输入文件名先规范化（小写转大写、'\\' 转 '/'），再算 32 位 hash。
该 hash 即 FLS0 TOC 里的 file_hash。
"""
from unicorn import *
from unicorn.x86_const import *

# sub_18020F760 的机器码（叶子函数，无外部调用）
CODE = bytes.fromhex(
    "48895c240848896c2410488974241848897c242041568b01488d590441b92889faf433ff41d1c1"
    "be0e47a837458bd141bb2bb458774181f2110b7b2648bd00000000ffffffff41bede77ebbd84c0"
    "0f844c010000a900ff00000f84b6000000a90000ff000f84a6000000a9000000ff0f84a3000000"
    "4433d833f08bc64c8bc7438d141a4923d64881ca01080402480fafd08bc2488bca48c1e920418d"
    "143285c98bf7410f95c081e2debb7e7d4c03c081ca214080004c03c1418bc34c85c54c8bdf400f"
    "95c6480fafd04103f0488bca48c1e9204803c94885cd8bc1410f95c34c03d88bc24c03d84c85dd"
    "74044183c3028b034883c30441d1c1458bd14181f2110b7b2684c00f8549ffffffe9900000000f"
    "b7c0eb030fb6c04433d833f08bc64c8bc7438d141a4923d64881ca01080402480fafd08bc2488b"
    "ca48c1e920418d143285c98bf7410f95c081e2debb7e7d4c03c081ca214080004c03c1418bc34c"
    "85c54c8bdf400f95c6480fafd04103f0488bca48c1e9204803c94885cd8bc1410f95c34c03d88b"
    "c24c03d84c85dd74044183c30241d1c1458bd14181f2110b7b264181f34844e79b81f64844e79b"
    "8bc64c8bc78bdf438d141a4923d64881ca01080402480fafd08bc2488bca48c1e920418d143285"
    "c94c8bd7410f95c081e2debb7e7d4c03c081ca214080004c03c1418bc34c85c50f95c3480fafd0"
    "4103d8488bca48c1e9204803c94885cd8bc1410f95c24c03d08bc24c03d04c85d574044183c202"
    "41d1c14181f2482cf4664181f1110b7b2681f3482cf4664c8bc78bc3438d14114923d64881ca01"
    "080402480fafd08bc2488bca48c1e920418d141985c9448bcf410f95c081e2debb7e7d4c03c081"
    "ca214080004c03c1418bc24c85c5410f95c1480fafd04503c8488bca48c1e9204803c94885cd8b"
    "c18bca400f95c74803f84803f94885fd740383c702488b5c24104133f9488b6c24188bc7488b7c"
    "2428488b742420415ec3"
)

_BASE = 0x140000000
_STACK = 0x200000000
_INBUF = 0x300000000
_SENT = 0x1111111111110000

_mu = Uc(UC_ARCH_X86, UC_MODE_64)
_mu.mem_map(_BASE, 0x10000)
_mu.mem_write(_BASE, CODE)
_mu.mem_map(_STACK, 0x100000)
_mu.mem_map(_INBUF, 0x10000)


def name_hash(name: str) -> int:
    """返回规范化文件名的 32 位 hash（= FLS0 file_hash）。"""
    s = name.upper().replace("\\", "/").encode("latin-1") + b"\x00" * 16
    _mu.mem_write(_INBUF, b"\x00" * 0x100)
    _mu.mem_write(_INBUF, s)
    sp = _STACK + 0x80000
    _mu.mem_write(sp, _SENT.to_bytes(8, "little"))
    _mu.reg_write(UC_X86_REG_RSP, sp)
    _mu.reg_write(UC_X86_REG_RCX, _INBUF)
    _mu.emu_start(_BASE, _SENT)
    return _mu.reg_read(UC_X86_REG_RAX) & 0xFFFFFFFF


if __name__ == "__main__":
    # mdata1 (= 关卡资源 1010101/json) 的 11 个 entry file_hash
    hashes = {0x21DD1A03, 0x3016099C, 0x3E2C490D, 0x61F80EDB, 0x65C60E29,
              0x69681BE9, 0x93167C23, 0xA298F892, 0xBDF05ABE, 0xBEC4156A, 0xED522F24}
    lines = ['1_0203001', '1_0203101', '1_0203201', '2_0001001', '2_0001101',
             '2_0001201', '3_0100001', '3_0100101', '3_0100201']
    extra = ['mapinfo', 'levelinfo', 'levelinfodif', 'mapdif', 'hideinfo']
    print("候选名 -> hash (.txt 后缀, 命中标 *)")
    hit = 0
    for n in lines + extra:
        for suf in ('.txt', '.json', ''):
            h = name_hash(n + suf)
            mark = ' *HIT*' if h in hashes else ''
            if mark:
                hit += 1
                print(f"  {n+suf:20s} -> 0x{h:08X}{mark}")
    print(f"命中 {hit} / {len(hashes)} 个目标 hash")
