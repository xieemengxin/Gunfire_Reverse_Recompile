# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1329.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1329.pyc
# Source Generated with Decompyle++
# File: st1329.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func425, Func427

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1326, 0, 0, None, None):
        cl_evact.EventGetTargetByConnectionInfo(oTarget, oEventCB, 1326)
        if cl_evcon.GetTargetNum(oTarget, oEventCB) >= 1:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, -7000, 0, '')


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1326, 0, 0, None, None):
        cl_evact.EventGetTargetByConnectionInfo(oTarget, oEventCB, 1326)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func427(*a, **{
'sKey': 1326 }))) > 0:
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func425(*a) * 7 / 10 / Func427(*a, **{
'sKey': 1326 })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, None, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 1329
    m_Name = '#NT#每日挑战6784玩家连接状态'
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
        5: CallBack5 }

