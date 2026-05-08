# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1218.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1218.pyc
# Source Generated with Decompyle++
# File: c1218.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_JAR, OBSTACLE_SCENEGOODS, WARRIOR_OBSTACLE_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_OBSTACLE_NORMAL
    m_Shape = 4126
    m_LimitDam = 100
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 100 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_JAR, OBSTACLE_SCENEGOODS)

