# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1061.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1061.pyc
# Source Generated with Decompyle++
# File: c1061.pyc (Python 3.6)

from cl_commondefines import WARRIOR_BEACON
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1061(oSummon):
    summonaction.SummonSetDieWithOwner(oSummon, 0)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1061
    m_Shape = 6966
    m_FightType = WARRIOR_BEACON
    m_BodyPart = ()
    m_Action = SummonAction1061
    m_BaseAttr = { }
    m_PerformList = ()

