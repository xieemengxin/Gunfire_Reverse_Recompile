# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4248.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4248.pyc
# Source Generated with Decompyle++
# File: p4248.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20026, 500, {
            'AbnormalSourceDam': 2500 }, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20028, 500, { }, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if not cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20027, 500, { }, 1, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20026, 1, None, None)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20028, 1, None, None)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20027, 1, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1403, 0, { }, -1, -1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1310: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20026, 1, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20028, 1, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 20027, 1, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1403, 0, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 4248
    m_Name = '苦难秘辛'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

