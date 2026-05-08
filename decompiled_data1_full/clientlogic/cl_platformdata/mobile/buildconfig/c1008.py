# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1008.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1008.pyc
# Source Generated with Decompyle++
# File: c1008.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_EXPLODE, OBSTACLE_JAR, OBSTACLE_NORMAL_EXPLODE, OBSTACLE_SCENEGOODS, WARRIOR_OBSTACLE_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_NORMAL
    m_Shape = 4301
    m_LimitDam = 100
    m_PerformList = (4009,)
    m_BaseAttr = {
        'HPMax': 99 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_JAR, OBSTACLE_EXPLODE, OBSTACLE_SCENEGOODS, OBSTACLE_NORMAL_EXPLODE)

