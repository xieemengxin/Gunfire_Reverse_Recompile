# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33569.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33569.pyc
# Source Generated with Decompyle++
# File: st33569.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER, OBJ_ALL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 44)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 20)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBImmuneDamageByType(oTarget, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER)
        cl_evact.EventClientBehavior(oTarget, oEventCB, 1123, 1)
        cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33569, (lambda *a: Func437(*a, **{
'sKey': 'MaxCount' })), 0, None)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33569
    m_Name = '琉璃之盾'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_ALL
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

