# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/suit/suit15305.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/suit/suit15305.pyc
# Source Generated with Decompyle++
# File: suit15305.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15305, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15305)


class CSuitData(CBaseSuitData):
    m_SID = 15305
    m_Name = '缚影长续'
    m_Condition = {
        1: (SUIT_BENEDICTION, 13564),
        2: (SUIT_TALENT, (3715, 3)),
        3: (SUIT_TALENT, (3713, 1)),
        4: (SUIT_TALENT, (3716, 1)),
        5: (SUIT_TALENT, (3718, 1)) }
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
    m_Career = 118
    m_ForeverCondition = []

