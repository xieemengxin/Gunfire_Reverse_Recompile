# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15101.pyc
# Source Generated with Decompyle++
# File: seasonsuit15101.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15167, 1)


def Action2(oTarget):
    return cl_action.RewardPassive(oTarget, 15167, 2)


def Action3(oTarget):
    return cl_action.RewardPassive(oTarget, 15167, 3)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15167)


def RemoveAction2(oTarget):
    return cl_action.RemovePassive(oTarget, 15167)


def RemoveAction3(oTarget):
    return cl_action.RemovePassive(oTarget, 15167)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15101
    m_Name = '暴击之眼'
    m_Condition = {
        1: (SUIT_RELIC, 5809),
        2: (SUIT_RELIC, 5820),
        3: (SUIT_RELIC, 5857),
        4: (SUIT_RELIC, 5799),
        5: (SUIT_RELIC, 5739),
        6: (SUIT_RELIC, 5803) }
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

