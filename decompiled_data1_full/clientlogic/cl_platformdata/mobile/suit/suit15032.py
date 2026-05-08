# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15032.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15032.pyc
# Source Generated with Decompyle++
# File: suit15032.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15032, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15032)


class CSuitData(CBaseSuitData):
    m_SID = 15032
    m_Name = '利刃出鞘'
    m_Condition = {
        1: (SUIT_TALENT, (2704, 1)),
        2: (SUIT_TALENT, (2703, 1)),
        3: (SUIT_RELIC, 5843),
        4: (SUIT_RELIC, 5757),
        5: (SUIT_RELIC, 5751) }
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
    m_Career = 109
    m_ForeverCondition = []

