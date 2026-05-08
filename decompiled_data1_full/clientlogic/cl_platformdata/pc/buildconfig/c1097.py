# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1097.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1097.pyc
# Source Generated with Decompyle++
# File: c1097.pyc (Python 3.6)

from cl_newformula import Func204, Func205, Func221
from cl_commondefines import WARRIOR_PROTEGE_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_PROTEGE_NORMAL
    m_Shape = 4252
    m_LimitDam = 0
    m_PerformList = (4231,)
    m_BaseAttr = {
        'HPMax': (lambda *a: 5000000 * ((Func205(*a) - 1) * 50 / 100 + 1) * ((Func204(*a) - 1) * 60 / 100 + 1) * (Func221(*a) * 15 / 100 + 1)) }
    m_InitFunc = None
    m_ClassifyList = ()

