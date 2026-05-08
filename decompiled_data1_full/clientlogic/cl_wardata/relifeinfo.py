# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/relifeinfo.pyc
# RelativePath: clientlogic/cl_wardata/relifeinfo.pyc
# Source Generated with Decompyle++
# File: relifeinfo.pyc (Python 3.6)

from math import ceil
from cl_newformula import Func201, Func202, Func205, Func220, Func678
g_RelifeInfo = {
    1001: {
        'SingleRelifeTimes': 1,
        'TeamRelifeTimes': 1,
        'SingleRelifeCost': {
            1: (lambda *a: ceil((Func205(*a) * 40 + min(56, Func201(*a) * 8 + Func202(*a) * 2) + Func220(*a) * 0.4 - 46) * Func678(*a) / 100)) },
        'TeamRelifeCost': {
            1: (lambda *a: ceil((Func205(*a) * 40 + min(56, Func201(*a) * 8 + Func202(*a) * 2) + Func220(*a) * 0.4 - 46) * Func678(*a) / 100)) } },
    1002: {
        'SingleRelifeTimes': 0,
        'TeamRelifeTimes': 0,
        'SingleRelifeCost': { },
        'TeamRelifeCost': { } },
    1003: {
        'SingleRelifeTimes': 1,
        'TeamRelifeTimes': 0,
        'SingleRelifeCost': {
            1: 0 },
        'TeamRelifeCost': {
            1: 0 } },
    1004: {
        'SingleRelifeTimes': 2,
        'TeamRelifeTimes': 1,
        'SingleRelifeCost': {
            1: (lambda *a: (Func205(*a) * 40 + Func201(*a) * 8 + Func202(*a) * 2 + Func220(*a) * 0.4 - 46) / 2),
            2: (lambda *a: max(20, ((Func205(*a) * 40 + Func201(*a) * 8 + Func202(*a) * 2 + Func220(*a) * 0.4 - 46) / 2) * 1.5)),
            3: (lambda *a: max(40, ((Func205(*a) * 40 + Func201(*a) * 8 + Func202(*a) * 2 + Func220(*a) * 0.4 - 46) / 2) * 2.25)),
            4: (lambda *a: max(60, ((Func205(*a) * 40 + Func201(*a) * 8 + Func202(*a) * 2 + Func220(*a) * 0.4 - 46) / 2) * 3.375)) },
        'TeamRelifeCost': {
            1: (lambda *a: Func205(*a) * 40 + Func201(*a) * 8 + Func202(*a) * 2 + Func220(*a) * 0.4 - 46) } } }

def GetRelifeInfo(iSid):
    return g_RelifeInfo.get(iSid, { })

