# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8026.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8026.pyc
# Source Generated with Decompyle++
# File: st8026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func205

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 8024, 0, { }, None)
    cl_action.StateAddState(oTarget, oLifeCycle, 8025, 0, { }, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 39255, -1, None):
        cl_evact.EventCBTriggerDropBullet(oTarget, oEventCB, {
            4502: 90,
            4503: 25,
            4504: 8,
            4508: 1 }, {
            4502: 10,
            4503: 10,
            4504: 10,
            4508: 10 }, 1, 1, { })


class CState(cl_state.CState):
    m_SID = 8026
    m_Name = '#NT#妖王放炮'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': (lambda *a: 225 - (Func205(*a) - 1) * 25),
        'firsttime': 150 }
    m_CBFuncAction = {
        0: CallBack0 }

