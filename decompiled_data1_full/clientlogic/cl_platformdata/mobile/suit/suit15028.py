# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15028.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15028.pyc
# Source Generated with Decompyle++
# File: suit15028.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15028, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15028)


class CSuitData(CBaseSuitData):
    m_SID = 15028
    m_Name = '力中暴力'
    m_Condition = {
        1: (SUIT_TALENT, (2311, 1)),
        2: (SUIT_RELIC, 5848),
        3: (SUIT_RELIC, 5720),
        4: (SUIT_RELIC, 5809),
        5: (SUIT_RELIC, 5739) }
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
    m_Career = 104
    m_ForeverCondition = []

