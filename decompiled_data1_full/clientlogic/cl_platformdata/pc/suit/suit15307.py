# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15307.pyc
# Source Generated with Decompyle++
# File: suit15307.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC, SUIT_TALENT
from .mobject import CBaseSuitData
import cl_action
import cl_condition

def Combination(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 2, [
        2,
        3,
        4,
        5]):
        return 1
    return 0


def Action(oTarget):
    return cl_action.RewardPassive(oTarget, 15307, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15307)


class CSuitData(CBaseSuitData):
    m_SID = 15307
    m_Name = '生生不息'
    m_Condition = {
        1: (SUIT_TALENT, (3809, 1)),
        2: (SUIT_RELIC, 5783),
        3: (SUIT_RELIC, 5811),
        4: (SUIT_RELIC, 5759),
        5: (SUIT_RELIC, 5878) }
    m_CondFunc = Combination
    m_Action = Action
    m_RemoveAction = RemoveAction
    m_CondInfo = {
        3: {
            1: 1,
            2: 0,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = 119
    m_ForeverCondition = []

