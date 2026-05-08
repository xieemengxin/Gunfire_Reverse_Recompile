# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1066.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1066.pyc
# Source Generated with Decompyle++
# File: c1066.pyc (Python 3.6)

from cl_commondefines import WARRIOR_TRAP_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1066(oBuild):
    buildaction.InitTrapEffectParam(oBuild, 75, 76)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_TRAP_NORMAL
    m_Shape = 4229
    m_LimitDam = 0
    m_PerformList = (1652,)
    m_BaseAttr = {
        'HPMax': 0 }
    m_InitFunc = BuildInitAction1066
    m_ClassifyList = ()

