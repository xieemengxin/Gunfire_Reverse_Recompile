# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8051.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8051.pyc
# Source Generated with Decompyle++
# File: st8051.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func369, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 8051) == 0 and cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SaveDamage', (lambda *a: Func369(*a) // 10))


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'SaveDamage' }) * 1 + 0), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, -1, -1, -1, None, None, None)


class CState(cl_state.CState):
    m_SID = 8051
    m_Name = '流血'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100,
        'cnt': 5 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

