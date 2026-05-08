# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suit/suit15017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suit/suit15017.pyc
# Source Generated with Decompyle++
# File: suit15017.pyc (Python 3.6)

from cl_commondefines import RELIC_TYPE_CURSE, SUIT_RELICTYPE
from .mobject import CBaseSuitData
import cl_action
import cl_condition

def Combination(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1):
        return 1
    return 0


def Action(oTarget):
    return cl_action.RewardPassive(oTarget, 15017, 1)


def RemoveAction(oTarget):
    return cl_action.RemovePassive(oTarget, 15017)


class CSuitData(CBaseSuitData):
    m_SID = 15017
    m_Name = '厄运扩散'
    m_Condition = {
        1: (SUIT_RELICTYPE, (RELIC_TYPE_CURSE, 3)) }
    m_CondFunc = Combination
    m_Action = Action
    m_RemoveAction = RemoveAction
    m_CondInfo = {
        1: {
            1: 1 } }
    m_Career = None
    m_ForeverCondition = []

