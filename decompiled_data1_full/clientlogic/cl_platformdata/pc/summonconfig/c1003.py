# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/summonconfig/c1003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/summonconfig/c1003.pyc
# Source Generated with Decompyle++
# File: c1003.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1003(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, None, None)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1003
    m_Shape = 5520
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1003
    m_BaseAttr = { }
    m_PerformList = ()

