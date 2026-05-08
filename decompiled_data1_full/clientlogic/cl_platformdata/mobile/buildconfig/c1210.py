# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1210.pyc
# Source Generated with Decompyle++
# File: c1210.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_EXPLODE, OBSTACLE_JAR, OBSTACLE_SCENEGOODS, OBSTACLE_THUNDER_EXPLODE, WARRIOR_TRAP_THUNDERBUCKET
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_TRAP_THUNDERBUCKET
    m_Shape = 4302
    m_LimitDam = 100
    m_PerformList = (5326,)
    m_BaseAttr = {
        'HPMax': 99 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_JAR, OBSTACLE_EXPLODE, OBSTACLE_SCENEGOODS, OBSTACLE_THUNDER_EXPLODE)

