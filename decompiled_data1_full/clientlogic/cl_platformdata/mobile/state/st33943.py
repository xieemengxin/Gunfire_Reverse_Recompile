# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33943.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33943.pyc
# Source Generated with Decompyle++
# File: st33943.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, HP_RADIO_ADD, HP_RADIO_SUB, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenHPThreshold(oTarget, oLifeCycle, 50, HP_RADIO_ADD, 0)
    cl_action.CommonListenHPThreshold(oTarget, oLifeCycle, 50, HP_RADIO_SUB, 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func429(*a, **{
'sArg': 'HighHPAddDam' })), DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: -Func429(*a, **{
'sArg': 'HighHPSubDam' })))


def CallBack1(oEventCB, oTarget):
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func429(*a, **{
'sArg': 'LowHPAddDam' })), DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: -Func429(*a, **{
'sArg': 'LowHPSubDam' })))


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetListenerHPRatio(oTarget, oEventCB) > 50:
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func429(*a, **{
'sArg': 'HighHPAddDam' })), DAM_MASK_ELEMENT, 1)
        cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: -Func429(*a, **{
'sArg': 'HighHPSubDam' })))
    else:
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func429(*a, **{
'sArg': 'LowHPAddDam' })), DAM_MASK_ELEMENT, 1)
        cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: -Func429(*a, **{
'sArg': 'LowHPSubDam' })))


class CState(cl_state.CState):
    m_SID = 33943
    m_Name = '#NT#小玖天赋迭代3912'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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

