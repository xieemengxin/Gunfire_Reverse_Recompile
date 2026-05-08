# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33435.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33435.pyc
# Source Generated with Decompyle++
# File: st33435.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func222, Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATESEASONSUITGRADE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func222(*a)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillNum', cl_action.CommonGetSuitConditionSpillNumByTag(oTarget, oEventCB.GetCBLifeCycle(), 6))
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func437(*a, **{
'sKey': 'SpillNum' })) }, 33435)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBCheckSuitActiveSourceHasTag(oTarget, oEventCB, 6):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 500 * Func404(*a) + 3000 * Func437(*a, **{
'sKey': 'SpillNum' })), 0, '')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckSuitHasTag(oTarget, oEventCB, 6):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillNum', cl_action.CommonGetSuitConditionSpillNumByTag(oTarget, oEventCB.GetCBLifeCycle(), 6))
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func437(*a, **{
'sKey': 'SpillNum' })) }, 33435)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillNum', cl_action.CommonGetSuitConditionSpillNumByTag(oTarget, oEventCB.GetCBLifeCycle(), 6))
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func437(*a, **{
'sKey': 'SpillNum' })) }, 33435)


class CState(cl_state.CState):
    m_SID = 33435
    m_Name = '威能连接'
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

