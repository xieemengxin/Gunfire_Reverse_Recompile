# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15069.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15069.pyc
# Source Generated with Decompyle++
# File: seasonsuit15069.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15069)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15069)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15069
    m_Name = '聚沙成塔'
    m_Condition = {
        1: (SUIT_TALENT, (3213, 1)),
        2: (SUIT_RELIC, 5858),
        3: (SUIT_RELIC, 5864),
        4: (SUIT_RELIC, 5799),
        5: (SUIT_RELIC, 5874) }
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
    m_Career = 113
    m_ForeverCondition = [
        5]
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 3 }

