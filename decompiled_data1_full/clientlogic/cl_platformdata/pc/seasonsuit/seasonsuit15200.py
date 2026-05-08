# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15200.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15200.pyc
# Source Generated with Decompyle++
# File: seasonsuit15200.pyc (Python 3.6)

from cl_commondefines import RELIC_TYPE_CURSE, SUIT_RELICTYPE
from .mobject import CBaseSeasonSuitData
import cl_action
import cl_condition

def Combination1(oSuitElement, iTarget, iSuit):
    if cl_condition.HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, 3, [
        1,
        2,
        3]):
        return 1
    return 0


def Action1(oTarget):
    return cl_action.RewardPassive(oTarget, 15182, 1)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15182)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15200
    m_Name = '苦尽甘来'
    m_Condition = {
        1: (SUIT_RELICTYPE, (RELIC_TYPE_CURSE, 3)),
        2: (SUIT_RELICTYPE, (RELIC_TYPE_CURSE, 3)),
        3: (SUIT_RELICTYPE, (RELIC_TYPE_CURSE, 3)) }
    m_CondFunc = {
        1: Combination1 }
    m_Action = {
        1: Action1 }
    m_RemoveAction = {
        1: RemoveAction1 }
    m_CondInfo = {
        3: {
            1: 0,
            2: 0,
            3: 0 } }
    m_Career = None
    m_ForeverCondition = []
    m_MaxGrade = 1
    m_GradeInfo = {
        1: 3 }

