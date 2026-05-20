#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""m1logic4.dll 资源文件名 hash —— 纯 Python 实现（无外部依赖）。

逆向自 m1logic4.dll：
  C_frscene.ReadFile(file, resource)
    -> sub_18020D350(file)   # 规范化：小写转大写、'\\' -> '/'
    -> sub_18020F760(name)   # 核心 hash（本文件复刻）
返回值即 FLS0 包内 entry 的 file_hash。

已用 unicorn 模拟原机器码对拍验证：1844 个真实资源名 + 8000 随机串，0 误差。

游戏内用法（放到 clientlogic/clinterface/cllib/namehash_pure.py）：
    import cllib.namehash_pure as nh
    h = nh.name_hash('1_0203001.txt')   # -> 0x21DD1A03
"""

_M = 0xFFFFFFFF
_M64 = 0xFFFFFFFFFFFFFFFF
_HI = 0xFFFFFFFF00000000
_K = 0x267B0B11
_M1, _O1 = 0xBDEB77DE, 0x2040801
_M2, _O2 = 0x7D7EBBDE, 0x804021
_C1, _C2 = 0x9BE74448, 0x66F42C48


def _rol32(x, n):
    x &= _M
    return ((x << n) | (x >> (32 - n))) & _M


def _fold_a(prod):
    lo = prod & _M
    hi = prod >> 32
    r = (1 if (hi & _M) else 0) + lo + hi
    return (r + (1 if (r & _HI) else 0)) & _M


def _fold_b(prod):
    lo = prod & _M
    two = 2 * (prod >> 32)
    r = (1 if (two & _HI) else 0) + (two & _M) + lo
    return ((r + 2) & _M) if (r & _HI) else (r & _M)


def _mix(v5, v6, v7, word):
    v8 = (word ^ v6) & _M
    v9 = (word ^ v5) & _M
    a = (((v7 + v8) & _M) & _M1) | _O1
    b = (((v7 + v9) & _M) & _M2) | _O2
    return _fold_a((v9 * a) & _M64), _fold_b((v8 * b) & _M64)


def _core(name):
    s = name.encode('latin-1') + b'\x00' * 8
    v4 = _rol32((-184907480) & _M, 1)
    v5, v6 = 0x37A8470E, 0x7758B42B
    v7 = v4 ^ _K
    p = 0
    if s[0]:
        while True:
            b0, b1, b2, b3 = s[p], s[p + 1], s[p + 2], s[p + 3]
            if b1 == 0:
                word = b0
            elif b2 == 0:
                word = b0 | (b1 << 8)
            elif b3 == 0:
                word = b0 | (b1 << 8) | (b2 << 16)
            else:
                word = b0 | (b1 << 8) | (b2 << 16) | (b3 << 24)
            v5, v6 = _mix(v5, v6, v7, word)
            v4 = _rol32(v4, 1)
            v7 = v4 ^ _K
            if b1 == 0 or b2 == 0 or b3 == 0:
                break
            p += 4
            if s[p] == 0:
                break
    v18 = (v6 ^ _C1) & _M
    v19 = (v5 ^ _C1) & _M
    a = (((v7 + v18) & _M) & _M1) | _O1
    b = (((v7 + v19) & _M) & _M2) | _O2
    v26 = (_fold_a((v19 * a) & _M64) ^ _C2) & _M
    v24 = (_fold_b((v18 * b) & _M64) ^ _C2) & _M
    v25 = (_rol32(v4, 1) ^ _K) & _M
    bf = (((v25 + v26) & _M) & _M2) | _O2
    v30 = _fold_b((v24 * bf) & _M64)
    af = (((v25 + v24) & _M) & _M1) | _O1
    v28 = _fold_a((v26 * af) & _M64)
    return (v28 ^ v30) & _M


def name_hash(filename):
    """filename 形如 '1_0203001.txt'（含后缀，逻辑层 json 资源后缀为 .txt）。"""
    return _core(filename.upper().replace('\\', '/'))


if __name__ == '__main__':
    assert name_hash('1_0203001.txt') == 0x21DD1A03
    assert name_hash('mapinfo.txt') == 0xA298F892
    assert name_hash('levelinfo.txt') == 0x65C60E29
    print('self-check ok')
