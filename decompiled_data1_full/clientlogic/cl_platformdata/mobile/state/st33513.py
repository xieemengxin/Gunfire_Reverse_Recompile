# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33513.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33513.pyc
# Source Generated with Decompyle++
# File: st33513.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437, Func597

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerformCDTimer(oTarget, oLifeCycle, 50, None)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a)))
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 140:
        cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', int(cl_action.CommonGetOwnerAttrBaseValue(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * 240))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AllAdd', (lambda *a: 140 + (Func404(*a) - 140) * 3))
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AllAdd', (lambda *a: Func404(*a)))
    cl_action.CommonChangePerformCDRate(oTarget, oEventCB.GetCBLifeCycle(), PERFORMCDRATE_TYPE_CAREER | PERFORMCDRATE_TYPE_PASSIVE | PERFORMCDRATE_TYPE_SHIFT, (lambda *a: 20 * Func437(*a, **{
'sKey': 'AllAdd' })), 0)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func437(*a, **{
'sKey': 'AllAdd' })) }, 33513)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckSuitActiveSourceHasTag(oTarget, oEventCB, 6):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20 * cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AllAdd'), 0, '')


class CState(cl_state.CState):
    m_SID = 33513
    m_Name = '迅捷转化'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

