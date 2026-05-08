# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2301.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2301.pyc
# Source Generated with Decompyle++
# File: p2301.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33887, 40, {
            'MoveSpeedMul': -8000 }, 0, 0, 0)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 20000, 0, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33887, 60, {
            'MoveSpeedMul': -8000 }, 0, 0, 0)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 30000, 0, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1670, 1, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33887, 100, {
            'MoveSpeedMul': -8000 }, 0, 0, 0)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 40000, 0, DAM_TYPE_PERFORM, None, None)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, 0, None):
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 40000, 5000, DAM_TYPE_PERFORM, None, None)


class CPerform(CCustomPerform):
    m_SID = 2301
    m_Name = '御雷要术'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 104

