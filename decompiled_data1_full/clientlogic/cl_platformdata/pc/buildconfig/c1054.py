# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1054.pyc
# Source Generated with Decompyle++
# File: c1054.pyc (Python 3.6)

from cl_commondefines import OBSTACLE_CURVEIGNORE, WARRIOR_STONEPILLAR
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_STONEPILLAR
    m_Shape = 4428
    m_LimitDam = 1000
    m_PerformList = (4119, 4295)
    m_BaseAttr = {
        'HPMax': 1000 }
    m_InitFunc = None
    m_ClassifyList = (OBSTACLE_CURVEIGNORE,)

