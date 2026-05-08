# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1436.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1436.pyc
# Source Generated with Decompyle++
# File: st1436.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) // 5 + 0))


class CState(cl_state.CState):
    m_SID = 1436
    m_Name = '重型法师'
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
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
        0: CallBack0 }

