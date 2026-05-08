# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15115.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15115.pyc
# Source Generated with Decompyle++
# File: seasonsuit15115.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 2, [
        1,
        2,
        3,
        4]):
        return 1
    return 0


def Combination2(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 4, [
        1,
        2,
        3,
        4]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15111, 1)


def Action2(oTarget):
    return cl_action.RewardPassive(oTarget, 15111, 2)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15111)


def RemoveAction2(oTarget):
    return cl_action.RemovePassive(oTarget, 15111)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15115
    m_Name = '超距救援'
    m_Condition = {
        1: (SUIT_RELIC, 5805),
        2: (SUIT_RELIC, 5806),
        3: (SUIT_RELIC, 5851),
        4: (SUIT_RELIC, 5855) }
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
        4: {
            1: 0,
            2: 0,
            3: 0,
            4: 0 } }
    m_Career = None
    m_ForeverCondition = []
    m_MaxGrade = 2
    m_GradeInfo = {
        1: 2,
        2: 4 }

