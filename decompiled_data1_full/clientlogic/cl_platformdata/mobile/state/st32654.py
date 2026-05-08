# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32654.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32654.pyc
# Source Generated with Decompyle++
# File: st32654.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3211) >= 3:
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            1: 1500,
            2: 8500 }, None)
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: -Func331(*a, **{
'sid': 3211 }) * 2000 - 1000), 0, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBImmuneDamageByType(oTarget, oEventCB, DAM_MASK_ELEMENT, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: -Func331(*a, **{
'sid': 3211 }) * 2000 - 1000), 0, '')


class CState(cl_state.CState):
    m_SID = 32654
    m_Name = '#NT#天赋3211'
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
        1: CallBack1,
        2: CallBack2 }

