# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15123.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonsuit/seasonsuit15123.pyc
# Source Generated with Decompyle++
# File: seasonsuit15123.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC
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
    return cl_action.RewardPassive(oTarget, 15117, 1)


def RemoveAction1(oTarget):
    return cl_action.RemovePassive(oTarget, 15117)


class CSuitData(CBaseSeasonSuitData):
    m_SID = 15123
    m_Name = '神秘连接'
    m_Condition = {
        1: (SUIT_RELIC, 5887),
        2: (SUIT_RELIC, 5888),
        3: (SUIT_RELIC, 5889) }
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

