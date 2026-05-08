# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1005.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1005.pyc
# Source Generated with Decompyle++
# File: c1005.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1005(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, 101, 500)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1005
    m_Shape = 4410
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1005
    m_BaseAttr = { }
    m_PerformList = ()

