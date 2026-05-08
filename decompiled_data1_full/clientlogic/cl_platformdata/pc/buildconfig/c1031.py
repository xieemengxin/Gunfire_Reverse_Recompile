# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1031.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1031.pyc
# Source Generated with Decompyle++
# File: c1031.pyc (Python 3.6)

from cl_commondefines import WARRIOR_OBSTACLE_TRANGATE
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

def BuildInitAction1031(oBuild):
    buildaction.InitBuildSetGateEffectParam(oBuild, 32, 34, 50, 0, 50, 0)


class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_TRANGATE
    m_Shape = 4414
    m_LimitDam = 1
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100000000 }
    m_InitFunc = BuildInitAction1031
    m_ClassifyList = ()

