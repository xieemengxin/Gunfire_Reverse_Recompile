# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1116.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1116.pyc
# Source Generated with Decompyle++
# File: c1116.pyc (Python 3.6)

from cl_newformula import Func201, Func204, Func221, Func244, Func304
from cl_commondefines import WARRIOR_SUMMON_STELE
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1116(oBuild):
    buildaction.InitSummonStelaParam(oBuild, 25, 25, 10, (lambda *a: (min(Func201(*a), 3) - 1) * 100 + (Func204(*a) + 1) * 100 / 2), 5000, {
        6101: 100,
        6102: 100,
        6103: 100,
        6104: 100,
        6105: 100,
        6106: 100,
        6107: 100,
        6108: 100,
        6109: 100,
        6110: 100,
        6111: 100,
        6112: 100,
        6115: 100 }, 1922, 240, 60, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.06 - min(Func201(*a), 4) * 0.7 / 100 - Func204(*a) * 0.4 / 100)))
    buildaction.BuildAddState(oBuild, 33109, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_SUMMON_STELE
    m_Shape = 5550
    m_LimitDam = 0
    m_PerformList = (7014, 4001)
    m_BaseAttr = {
        'HPMax': (lambda *a: (36000000 + (Func201(*a) - 2) * 18000000 + (Func244(*a) - 6) * 4000000) * min(20, -3 + Func201(*a) * 2) * (1 + 0.7 * Func221(*a) + min(Func221(*a), 1)) * (1 + (Func204(*a) - 1) * 1.7)) }
    m_InitFunc = BuildInitAction1116
    m_ClassifyList = ()

