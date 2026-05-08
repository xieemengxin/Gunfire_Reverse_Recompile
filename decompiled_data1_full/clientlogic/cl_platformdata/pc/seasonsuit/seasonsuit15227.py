# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15227.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15227.pyc
# Source Generated with Decompyle++
# File: seasonsuit15227.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC, SUIT_TALENT
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 2, [
        2,
        3,
        4,
        5]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15303, 1)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15303)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15227
    m_Name = '气涌强攻'
    m_Condition = {
        1: (SUIT_TALENT, (3714, 1)),
        2: (SUIT_RELIC, 5884),
        3: (SUIT_RELIC, 5882),
        4: (SUIT_RELIC, 5876),
        5: (SUIT_RELIC, 5710) }
    m_CondFunc = {
        1: Combination1 }
    m_Action = {
        1: Action1 }
    m_RemoveAction = {
        1: RemoveAction1 }
    m_CondInfo = {
        3: {
            1: 1,
            2: 0,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = 118
    m_ForeverCondition = []
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 3 }

