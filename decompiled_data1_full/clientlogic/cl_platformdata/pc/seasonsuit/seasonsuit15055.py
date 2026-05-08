# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15055.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15055.pyc
# Source Generated with Decompyle++
# File: seasonsuit15055.pyc (Python 3.6)

from cl_commondefines import SUIT_BENEDICTION, SUIT_TALENT
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 2) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 1, [
        3,
        4,
        5]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15055)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15055)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15055
    m_Name = '破军之威'
    m_Condition = {
        1: (SUIT_BENEDICTION, 13535),
        2: (SUIT_TALENT, (2220, 3)),
        3: (SUIT_TALENT, (2205, 1)),
        4: (SUIT_TALENT, (2221, 1)),
        5: (SUIT_TALENT, (2203, 1)) }
    m_CondFunc = {
        1: Combination1 }
    m_Action = {
        1: Action1 }
    m_RemoveAction = {
        1: RemoveAction1 }
    m_CondInfo = {
        3: {
            1: 1,
            2: 1,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = 103
    m_ForeverCondition = []
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 3 }

