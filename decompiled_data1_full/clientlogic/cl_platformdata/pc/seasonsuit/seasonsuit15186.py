# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15186.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15186.pyc
# Source Generated with Decompyle++
# File: seasonsuit15186.pyc (Python 3.6)

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


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15178, 1)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15178)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15186
    m_Name = '应急防护'
    m_Condition = {
        1: (SUIT_RELIC, 5787),
        2: (SUIT_RELIC, 5705),
        3: (SUIT_RELIC, 5732),
        4: (SUIT_RELIC, 5773) }
    m_CondFunc = {
        1: Combination1 }
    m_Action = {
        1: Action1 }
    m_RemoveAction = {
        1: RemoveAction1 }
    m_CondInfo = {
        2: {
            1: 0,
            2: 0,
            3: 0,
            4: 0 } }
    m_Career = None
    m_ForeverCondition = [
        2]
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 2 }

