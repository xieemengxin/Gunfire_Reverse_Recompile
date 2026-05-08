# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1113.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1113.pyc
# Source Generated with Decompyle++
# File: c1113.pyc (Python 3.6)

from cl_commondefines import WARRIOR_OBSTACLE_STATICTRAN
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1113(oBuild):
    buildaction.InitBuildSetGateEffectParam(oBuild, 35, 36, 50, 0, 50, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_STATICTRAN
    m_Shape = 7001
    m_LimitDam = 1
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100000000 }
    m_InitFunc = BuildInitAction1113
    m_ClassifyList = ()

