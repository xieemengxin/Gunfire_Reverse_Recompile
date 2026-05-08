# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1040.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1040.pyc
# Source Generated with Decompyle++
# File: c1040.pyc (Python 3.6)

from cl_commondefines import WARRIOR_OBSTACLE_SLIDEDOOR
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1040(oBuild):
    buildaction.InitBuildSetGateEffectParam(oBuild, 38, 37, 0, 0, 0, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_SLIDEDOOR
    m_Shape = 4418
    m_LimitDam = 1
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100000000 }
    m_InitFunc = BuildInitAction1040
    m_ClassifyList = ()

