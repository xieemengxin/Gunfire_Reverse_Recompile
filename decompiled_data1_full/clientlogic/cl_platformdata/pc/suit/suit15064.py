# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15064.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15064.pyc
# Source Generated with Decompyle++
# File: suit15064.pyc (Python 3.6)

from cl_commondefines import SUIT_BENEDICTION, SUIT_TALENT
from .mobject import CBaseSuitData
import cl_action
import cl_condition

def Combination(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 2) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 1, [
        3,
        4,
        5]):
        return 1
    return 0


def Action(oTarget):
    return cl_action.RewardPassive(oTarget, 15064, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15064)


class CSuitData(CBaseSuitData):
    m_SID = 15064
    m_Name = '灵火图腾'
    m_Condition = {
        1: (SUIT_BENEDICTION, 13529),
        2: (SUIT_TALENT, (3114, 3)),
        3: (SUIT_TALENT, (3108, 1)),
        4: (SUIT_TALENT, (3117, 1)),
        5: (SUIT_TALENT, (3118, 1)) }
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

