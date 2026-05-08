# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1060.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1060.pyc
# Source Generated with Decompyle++
# File: c1060.pyc (Python 3.6)

from cl_commondefines import WARRIOR_TRAP_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1060(oBuild):
    buildaction.InitTrapEffectParam(oBuild, 75, 76)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_TRAP_NORMAL
    m_Shape = 4227
    m_LimitDam = 0
    m_PerformList = (1611,)
    m_BaseAttr = {
        'HPMax': 0 }
    m_InitFunc = BuildInitAction1060
    m_ClassifyList = ()

