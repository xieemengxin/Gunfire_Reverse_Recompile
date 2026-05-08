# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15221.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15221.pyc
# Source Generated with Decompyle++
# File: seasonsuit15221.pyc (Python 3.6)

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
    return cl_action.RewardPassive(oTarget, 15307, 1)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15307)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15221
    m_Name = '生生不息'
    m_Condition = {
        1: (SUIT_TALENT, (3809, 1)),
        2: (SUIT_RELIC, 5783),
        3: (SUIT_RELIC, 5811),
        4: (SUIT_RELIC, 5759),
        5: (SUIT_RELIC, 5878) }
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
    m_Career = 119
    m_ForeverCondition = []
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 3 }

