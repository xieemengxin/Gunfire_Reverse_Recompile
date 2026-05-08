# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1046.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1046.pyc
# Source Generated with Decompyle++
# File: c1046.pyc (Python 3.6)

from cl_commondefines import WARRIOR_OBSTACLE_STATICTRAN
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1046(oBuild):
    buildaction.InitBuildSetGateEffectParam(oBuild, 41, 40, 0, 0, 50, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_STATICTRAN
    m_Shape = 4401
    m_LimitDam = 1
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100000000 }
    m_InitFunc = BuildInitAction1046
    m_ClassifyList = ()

