# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33587.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33587.pyc
# Source Generated with Decompyle++
# File: st33587.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func452, Func651, Func756

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 3:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ActNum' }))) == cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'ActNum' }))) and cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'StateSID') == 1091:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack1(oEventCB, oTarget):
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -3, None)
    cl_evact.EventCBCustomUsePerform(oTarget, oEventCB, 1971, {
        'vStart': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExplodePos') }, {
        'Radius': (lambda *a: Func756(*a, **{
'sAttr': 'Radius' }) * 100 + 400) }, (lambda *a: Func452(*a)))


class CState(cl_state.CState):
    m_SID = 33587
    m_Name = '#NT#狱裂骨龙额外爆炸'
    m_Type = STATE_CLS_HELP
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
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

