# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13513.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13513.pyc
# Source Generated with Decompyle++
# File: p13513.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 2, 0, 0)
    cl_action.CommonIgnoreAttrChangeFromWeapon(oWarrior, oLifeCycle, 'Hold', 'MoveSpeed', 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32004):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32977, 0, { }, 1, 1, None)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32978, -1, -1, -1):
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32978, None, 0, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32978, 0, { }, 1, 0, None)
            if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32977, -1, -1, -1):
                cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32977, None, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32977, 0, { }, 1, 1, None)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32978, -1, -1, -1):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32978, None, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32978, 0, { }, 1, 0, None)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32977, -1, -1, -1):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 32977, None, 0, None)


class CPerform(CCustomPerform):
    m_SID = 13513
    m_Name = '兵贵神速'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 101

