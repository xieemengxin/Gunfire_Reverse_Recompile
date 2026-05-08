# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1008.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1008.pyc
# Source Generated with Decompyle++
# File: c1008.pyc (Python 3.6)

from cl_commondefines import WARRIOR_CIRCLE
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1008(oSummon):
    summonaction.SummonSetCircleParam(oSummon, 500, 2, 101, 500)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1008
    m_Shape = 4413
    m_FightType = WARRIOR_CIRCLE
    m_BodyPart = ()
    m_Action = SummonAction1008
    m_BaseAttr = { }
    m_PerformList = ()

