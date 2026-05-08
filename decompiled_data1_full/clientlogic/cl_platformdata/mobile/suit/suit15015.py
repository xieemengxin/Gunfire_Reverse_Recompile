# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15015.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15015.pyc
# Source Generated with Decompyle++
# File: suit15015.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC
from .mobject import CBaseSuitData
import cl_action
import cl_condition

def Combination(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 3, [
        1,
        2,
        3,
        4,
        5]):
        return 1
    return 0


def Action(oTarget):
    return cl_action.RewardPassive(oTarget, 15015, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15015)


class CSuitData(CBaseSuitData):
    m_SID = 15015
    m_Name = '长跑健将'
    m_Condition = {
        1: (SUIT_RELIC, 5777),
        2: (SUIT_RELIC, 5774),
        3: (SUIT_RELIC, 5754),
        4: (SUIT_RELIC, 5819),
        5: (SUIT_RELIC, 5804) }
    m_CondFunc = Combination
    m_Action = Action
    m_RemoveAction = RemoveAction
    m_CondInfo = {
        3: {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = None
    m_ForeverCondition = []

