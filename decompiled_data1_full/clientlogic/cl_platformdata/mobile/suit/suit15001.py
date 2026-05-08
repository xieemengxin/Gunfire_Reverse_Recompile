# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15001.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15001.pyc
# Source Generated with Decompyle++
# File: suit15001.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_NORMAL, SUIT_RELIC, SUIT_WEAPONDAMAGE
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
    return cl_action.RewardPassive(oTarget, 15001, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15001)


class CSuitData(CBaseSuitData):
    m_SID = 15001
    m_Name = '火焰转化'
    m_Condition = {
        1: (SUIT_WEAPONDAMAGE, DAM_TYPE_NORMAL),
        2: (SUIT_RELIC, 5781),
        3: (SUIT_RELIC, 5795),
        4: (SUIT_RELIC, 5779),
        5: (SUIT_RELIC, 5741) }
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
    m_Career = None
    m_ForeverCondition = []

