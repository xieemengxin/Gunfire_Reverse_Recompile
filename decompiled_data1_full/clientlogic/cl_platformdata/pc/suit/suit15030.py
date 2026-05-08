# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15030.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15030.pyc
# Source Generated with Decompyle++
# File: suit15030.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15030, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15030)


class CSuitData(CBaseSuitData):
    m_SID = 15030
    m_Name = '闪电鞭索'
    m_Condition = {
        1: (SUIT_TALENT, (2316, 1)),
        2: (SUIT_RELIC, 5790),
        3: (SUIT_RELIC, 5718),
        4: (SUIT_RELIC, 5834),
        5: (SUIT_RELIC, 5810) }
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
    m_ForeverCondition = [
        5]

