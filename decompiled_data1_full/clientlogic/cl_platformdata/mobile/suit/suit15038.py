# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15038.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15038.pyc
# Source Generated with Decompyle++
# File: suit15038.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15038, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15038)


class CSuitData(CBaseSuitData):
    m_SID = 15038
    m_Name = '烈火狐踪'
    m_Condition = {
        1: (SUIT_TALENT, (3113, 1)),
        2: (SUIT_TALENT, (3115, 1)),
        3: (SUIT_RELIC, 5711),
        4: (SUIT_RELIC, 5766),
        5: (SUIT_RELIC, 5725) }
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
    m_Career = 112
    m_ForeverCondition = []

