# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1007.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1007.pyc
# Source Generated with Decompyle++
# File: c1007.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1007(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, 101, 500)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1007
    m_Shape = 4412
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1007
    m_BaseAttr = { }
    m_PerformList = ()

