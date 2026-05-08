# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1004.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1004.pyc
# Source Generated with Decompyle++
# File: c1004.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1004(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, 101, 500)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1004
    m_Shape = 4409
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1004
    m_BaseAttr = { }
    m_PerformList = ()

