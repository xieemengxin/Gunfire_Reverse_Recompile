# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32419.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32419.pyc
# Source Generated with Decompyle++
# File: st32419.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 1:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 2 * Func404(*a) * Func331(*a, **{
'sid': 2508 }) * 100 + 100 * Func404(*a)), 0, 0, '')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 10 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2508) >= 3:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 2 * Func404(*a)))


class CState(cl_state.CState):
    m_SID = 32419
    m_Name = '#NT#充能弹药效果'
    m_DieRemove = 1
    m_IsShow = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

