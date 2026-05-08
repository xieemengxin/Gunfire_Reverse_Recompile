# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/buildconfig/c1095.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/buildconfig/c1095.pyc
# Source Generated with Decompyle++
# File: c1095.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_CORRISION_EXPLODE, OBSTACLE_EXPLODE, OBSTACLE_JAR, OBSTACLE_SCENEGOODS, WARRIOR_OBSTACLE_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_NORMAL
    m_Shape = 6965
    m_LimitDam = 100
    m_PerformList = (4263,)
    m_BaseAttr = {
        'HPMax': 100 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_JAR, OBSTACLE_EXPLODE, OBSTACLE_SCENEGOODS, OBSTACLE_CORRISION_EXPLODE)

