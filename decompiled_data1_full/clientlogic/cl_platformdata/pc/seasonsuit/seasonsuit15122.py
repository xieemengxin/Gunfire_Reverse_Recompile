# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15122.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15122.pyc
# Source Generated with Decompyle++
# File: seasonsuit15122.pyc (Python 3.6)

from cl_platformdata.custom.seasonsuit.customaction import CustomAction15122 as CustomAction
from cl_commondefines import SUIT_RELIC
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 1, [
        2,
        3,
        4,
        5]):
        return 1
    return 0


def Combination2(oSuitElement, iTarget, iSuit):
    if cl_condition.HasCondition(oSuitElement, iTarget, iSuit, 1) and cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 4, [
        2,
        3,
        4,
        5]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.ReplaceCoreRelic(oTarget, 15122, 1)


def Action2(oTarget):
    return cl_action.ReplaceCoreRelic(oTarget, 15122, 2)


def RemoveAction1(oTarget):
    return cl_action.RemoveCoreRelic(oTarget, 15122)


def RemoveAction2(oTarget):
    return cl_action.RemoveCoreRelic(oTarget, 15122)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15122
    m_Name = '损余奉缺'
    m_Condition = {
        1: (SUIT_RELIC, 5878),
        2: (SUIT_RELIC, 5827),
        3: (SUIT_RELIC, 5811),
        4: (SUIT_RELIC, 5790),
        5: (SUIT_RELIC, 5718) }
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
        5: {
            1: 1,
            2: 0,
            3: 0,
            4: 0,
            5: 0 } }
    m_Career = None
    m_ForeverCondition = []
    m_MaxGrade = 2
    m_GradeInfo = {
        1: 2,
        2: 5 }

