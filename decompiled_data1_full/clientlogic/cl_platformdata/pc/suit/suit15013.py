# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15013.pyc
# Source Generated with Decompyle++
# File: suit15013.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15013, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15013)


class CSuitData(CBaseSuitData):
    m_SID = 15013
    m_Name = '元素狂热'
    m_Condition = {
        1: (SUIT_RELIC, 5795),
        2: (SUIT_RELIC, 5796),
        3: (SUIT_RELIC, 5797),
        4: (SUIT_RELIC, 5714),
        5: (SUIT_RELIC, 5713) }
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

