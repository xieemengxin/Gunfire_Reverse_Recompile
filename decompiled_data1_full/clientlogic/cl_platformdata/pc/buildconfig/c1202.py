# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/buildconfig/c1202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/buildconfig/c1202.pyc
# Source Generated with Decompyle++
# File: c1202.pyc (Python 3.6)

from cl_newformula import Func669
from cl_commondefines import WARRIOR_MONSTERBUILD
import cl_wardata.buildaction as buildaction
from . import buildconfigdata

class CBuildData(buildconfigdata.CBuildData):
    m_FightType = WARRIOR_MONSTERBUILD
    m_Shape = 5569
    m_LimitDam = 0
    m_PerformList = (1961, 14604, 14605)
    m_BaseAttr = {
        'HPMax': (lambda *a: Func669(*a) * 0.1) }
    m_InitFunc = None
    m_ClassifyList = ()

