# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15114.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15114.pyc
# Source Generated with Decompyle++
# File: seasonsuit15114.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 3, [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9]):
        return 1
    return 0


def Combination2(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 6, [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15103, 1)


def Action2(oTarget):
    return cl_action.RewardPassive(oTarget, 15103, 2)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15103)


def RemoveAction2(oTarget):
    return cl_action.RemovePassive(oTarget, 15103)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15114
    m_Name = '推进套装'
    m_Condition = {
        1: (SUIT_RELIC, 5770),
        2: (SUIT_RELIC, 5798),
        3: (SUIT_RELIC, 5761),
        4: (SUIT_RELIC, 5818),
        5: (SUIT_RELIC, 5760),
        6: (SUIT_RELIC, 5793) }
    m_CondFunc = {
        1: Combination1,
        2: Combination2 }
    m_Action = {
        1: Action1,
        2: Action2 }
    m_RemoveAction = {
        1: RemoveAction1,
        2: RemoveAction2 }
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
    m_MaxGrade = 2
    m_GradeInfo = {
        1: 3,
        2: 6 }

