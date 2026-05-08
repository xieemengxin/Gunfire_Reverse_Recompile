# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8122.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8122.pyc
# Source Generated with Decompyle++
# File: st8122.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREVERTIGO, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 2500, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'AttSpeed', -2000, 0, 0)
    cl_action.CommonChangeAllAtivePerformAttr(oTarget, oLifeCycle, 'ColdTime', -2000, 0)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetTargetConquerStatus(oTarget, oEventCB, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1605: 1,
        1609: 1,
        1658: 1 }, 0, 0):
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func589(*a) * 20 / 100))


class CState(cl_state.CState):
    m_SID = 8122
    m_Name = '#NT#妖化怪-强化（普通妖化怪）'
    m_IsShow = 1
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

