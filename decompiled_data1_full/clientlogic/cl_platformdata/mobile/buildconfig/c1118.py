# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1118.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1118.pyc
# Source Generated with Decompyle++
# File: c1118.pyc (Python 3.6)

from cl_commondefines import WARRIOR_TRAP_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1118(oBuild):
    buildaction.InitThunderTrapCenterPos(oBuild)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_TRAP_NORMAL
    m_Shape = 4310
    m_LimitDam = 0
    m_PerformList = (1926,)
    m_BaseAttr = {
        'HPMax': 0 }
    m_InitFunc = BuildInitAction1118
    m_ClassifyList = ()

