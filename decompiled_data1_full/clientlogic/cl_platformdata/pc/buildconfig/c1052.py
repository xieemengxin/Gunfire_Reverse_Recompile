# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1052.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1052.pyc
# Source Generated with Decompyle++
# File: c1052.pyc (Python 3.6)

from cl_commondefines import WARRIOR_OBSTACLE_STATICTRAN
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1052(oBuild):
    buildaction.InitBuildSetGateEffectParam(oBuild, 35, 36, 50, 0, 50, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_STATICTRAN
    m_Shape = 4426
    m_LimitDam = 1
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100000000 }
    m_InitFunc = BuildInitAction1052
    m_ClassifyList = ()

