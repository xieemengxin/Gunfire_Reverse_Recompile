# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1043.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1043.pyc
# Source Generated with Decompyle++
# File: c1043.pyc (Python 3.6)

from cl_newformula import Func201, Func204, Func205, Func221
from cl_commondefines import WARRIOR_PROTEGE_NORMAL
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_PROTEGE_NORMAL
    m_Shape = 5532
    m_LimitDam = 0
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': (lambda *a: 120000 + (Func201(*a) - 1) * 150000 + (120000 + (Func201(*a) - 1) * 150000) * (Func205(*a) + 0.15 * Func221(*a) - 1) * 0.8 + (120000 + (Func201(*a) - 1) * 150000) * (Func204(*a) - 1) * 0.4) }
    m_InitFunc = None
    m_ClassifyList = ()

