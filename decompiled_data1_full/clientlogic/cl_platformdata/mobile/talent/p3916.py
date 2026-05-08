# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3916.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3916.pyc
# Source Generated with Decompyle++
# File: p3916.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33738, 0, 1, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33738, 0, {
            'TransDamFactor': 40 }, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33738, 0, 1, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33738, 0, {
            'TransDamFactor': 80 }, 1, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33738, 0, 1, 0, 0) or cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB)) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '33738AddSubSpeedStateFlag', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, '33738AddSubSpeedStateFlag', 1, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1012, 500, {
            'MoveSpeedMul': -3000 }, 0, 1, 0)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33738, 0, {
            'TransDamFactor': 120 }, 1, 1, 0)
        if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '33738AddSubSpeedStateFlag', 0) == 0:
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, '33738AddSubSpeedStateFlag', 1, 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1012, 500, {
                'MoveSpeedMul': -3000 }, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3916
    m_Name = '#NT#觉醒占位'
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
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 120

