# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32860.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32860.pyc
# Source Generated with Decompyle++
# File: st32860.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func543, Func560

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 1)
    elif cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_NORMAL):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 2)
    elif cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 3)
    elif cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: Func560(*a))):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 4)
    else:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func543(*a, **{
'dWeight': {
1: 1,
2: 1,
3: 1 } })))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckQuality(oTarget, oEventCB, QUALITY_TYPE_CURSE):
        if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: Func560(*a))):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 4)
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func543(*a, **{
'dWeight': {
1: 1,
2: 1,
3: 1 } })))


class CState(cl_state.CState):
    m_SID = 32860
    m_Name = '#NT#赌侠W2觉醒3级'
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
        3: CallBack3 }

