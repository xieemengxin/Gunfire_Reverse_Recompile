# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15093.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15093.pyc
# Source Generated with Decompyle++
# File: suit15093.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15075, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15075)


class CSuitData(CBaseSuitData):
    m_SID = 15093
    m_Name = '#NT#究极进化'
    m_Condition = {
        1: (SUIT_BENEDICTION, 13571),
        2: (SUIT_TALENT, (3306, 3)),
        3: (SUIT_TALENT, (3302, 1)),
        4: (SUIT_TALENT, (3304, 1)),
        5: (SUIT_TALENT, (3903, 1)) }
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
    m_Career = 120
    m_ForeverCondition = []

