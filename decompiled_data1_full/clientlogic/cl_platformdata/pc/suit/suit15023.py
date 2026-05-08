# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15023.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15023.pyc
# Source Generated with Decompyle++
# File: suit15023.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC, SUIT_TALENT
from .mobject import CBaseSuitData
import cl_action
import cl_condition

def Combination(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 1, [
        3,
        4,
        5]) and cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 2):
        return 1
    return 0


def Action(oTarget):
    return cl_action.RewardPassive(oTarget, 15023, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15023)


class CSuitData(CBaseSuitData):
    m_SID = 15023
    m_Name = '禁锢烟雾'
    m_Condition = {
        1: (SUIT_TALENT, (2124, 1)),
        2: (SUIT_TALENT, (2102, 1)),
        3: (SUIT_RELIC, 5834),
        4: (SUIT_RELIC, 5790),
        5: (SUIT_RELIC, 5718) }
    m_CondFunc = Combination
    m_Action = Action
    m_RemoveAction = RemoveAction
    m_CondInfo = {
        3: {
            1: 1,
            2: 1,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = 102
    m_ForeverCondition = []

