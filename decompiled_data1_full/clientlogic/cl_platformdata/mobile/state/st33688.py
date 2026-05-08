# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33688.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33688.pyc
# Source Generated with Decompyle++
# File: st33688.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437, Func526, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33688, 5, 'AdditionRatio')
    cl_action.CommonChangeStateMaxCount(oTarget, oLifeCycle, 33639, 0, 10000, 1, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33639, 1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'AdditionRatio' }) * Func526(*a)))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33639:
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func526(*a) * Func437(*a, **{
'sKey': 'AdditionRatio' })) })


def CallBack2(oEventCB, oTarget):
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func526(*a) * Func437(*a, **{
'sKey': 'AdditionRatio' })) })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33688
    m_Name = '抱元守一'
    m_IsShow = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 400,
        'firsttime': 400 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

