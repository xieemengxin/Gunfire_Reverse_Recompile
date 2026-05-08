# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/summonconfig/c1006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/summonconfig/c1006.pyc
# Source Generated with Decompyle++
# File: c1006.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1006(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, 101, 500)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1006
    m_Shape = 4411
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1006
    m_BaseAttr = { }
    m_PerformList = ()

