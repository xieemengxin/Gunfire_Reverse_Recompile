# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32373.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32373.pyc
# Source Generated with Decompyle++
# File: st32373.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func340, Func404, Func429, Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 60:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }) * 1000 + Func404(*a) * 50), 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func404(*a) * 50), 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBRecordMoveDis(oTarget, oEventCB, 'st32373', OBJECT_OWNER, 0)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }) * Func340(*a, **{
'sKey': 'st32373' }))) >= 100:
        cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'PF5880', 1)
        cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 32373, (lambda *a: Func598(*a, **{
'sKey': 'PF5880' })), None)
        cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st32373', OBJECT_OWNER, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB):
        cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st32373', OBJECT_OWNER, 0, 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32373, 0) * 5 + oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect') * 100 }, 32373)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evact.EventCBGetTargetStateCount(oTarget, oEventCB, 32373, 0) * 5 }, 32373)


class CState(cl_state.CState):
    m_SID = 32373
    m_Name = '愈行愈速'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

