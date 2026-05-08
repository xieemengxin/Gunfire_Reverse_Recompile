# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32629.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32629.pyc
# Source Generated with Decompyle++
# File: st32629.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_CLASS, DAM_MASK_ELEMENT, DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func404(*a) * (200 * Func331(*a, **{
'sid': 5421 }) + 400)), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func404(*a) * (200 * Func331(*a, **{
'sid': 5421 }) + 400)), 0)
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, (lambda *a: Func404(*a) * 300 * Func331(*a, **{
'sid': 5421 })), DAM_MASK_CLASS, DAM_MASK_ELEMENT, -1)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    if oTarget.HP() > 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -2, None)


class CState(cl_state.CState):
    m_SID = 32629
    m_Name = '真气护体'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

