# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1101.pyc
# Source Generated with Decompyle++
# File: c1101.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_CURVEIGNORE, WARRIOR_PERFORM_BUILD
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_PERFORM_BUILD
    m_Shape = 4263
    m_LimitDam = 0
    m_PerformList = (4310,)
    m_BaseAttr = {
        'HPMax': 1000 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_CURVEIGNORE,)

