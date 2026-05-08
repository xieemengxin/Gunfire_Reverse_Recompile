# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15082.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15082.pyc
# Source Generated with Decompyle++
# File: suit15082.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15087, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15087)


class CSuitData(CBaseSuitData):
    m_SID = 15082
    m_Name = '巨型霜冻'
    m_Condition = {
        1: (SUIT_TALENT, (3514, 1)),
        2: (SUIT_RELIC, 5811),
        3: (SUIT_RELIC, 5830),
        4: (SUIT_RELIC, 5826),
        5: (SUIT_RELIC, 5849) }
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
    m_Career = 116
    m_ForeverCondition = []

