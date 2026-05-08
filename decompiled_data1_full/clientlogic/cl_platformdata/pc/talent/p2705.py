# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2705.pyc
# Source Generated with Decompyle++
# File: p2705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_VICTIM, SWORD_DOUBLE_DAMAGE, SWORD_TREBLE_DAMAGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1313: 1,
        8503: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None):
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                2: 4000,
                3: 2000 }, None)
        else:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                2: 4000 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 4000,
            3: 2000 }, None)
    else:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            2: 4000 }, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 10000, DAM_TYPE_PERFORM, None, None)
    cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, SWORD_DOUBLE_DAMAGE)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, 20000, DAM_TYPE_PERFORM, None, None)
    cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, SWORD_TREBLE_DAMAGE)


class CPerform(CCustomPerform):
    m_SID = 2705
    m_Name = '凝光剑气'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 109

