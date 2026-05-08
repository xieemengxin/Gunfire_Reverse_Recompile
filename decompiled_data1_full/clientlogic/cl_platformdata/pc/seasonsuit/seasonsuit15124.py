# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15124.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15124.pyc
# Source Generated with Decompyle++
# File: seasonsuit15124.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 2, [
        1,
        2,
        3,
        4,
        5,
        6]):
        return 1
    return 0


def Combination2(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 4, [
        1,
        2,
        3,
        4,
        5,
        6]):
        return 1
    return 0


def Combination3(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 6, [
        1,
        2,
        3,
        4,
        5,
        6]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15201, 1)


def Action2(oTarget):
    return cl_action.RewardPassive(oTarget, 15201, 2)


def Action3(oTarget):
    return cl_action.RewardPassive(oTarget, 15201, 3)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15201)


def RemoveAction2(oTarget):
    return cl_action.RemovePassive(oTarget, 15201)


def RemoveAction3(oTarget):
    return cl_action.RemovePassive(oTarget, 15201)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15124
    m_Name = '迅影流星'
    m_Condition = {
        1: (SUIT_RELIC, 5729),
        2: (SUIT_RELIC, 5760),
        3: (SUIT_RELIC, 5819),
        4: (SUIT_RELIC, 5743),
        5: (SUIT_RELIC, 5880),
        6: (SUIT_RELIC, 5770) }
    m_CondFunc = {
        1: Combination1,
        2: Combination2,
        3: Combination3 }
    m_Action = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_RemoveAction = {
        1: RemoveAction1,
        2: RemoveAction2,
        3: RemoveAction3 }
    m_CondInfo = {
        6: {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0 } }
    m_Career = None
    m_ForeverCondition = []
    m_MaxGrade = 3
    m_GradeInfo = {
        1: 2,
        2: 4,
        3: 6 }

