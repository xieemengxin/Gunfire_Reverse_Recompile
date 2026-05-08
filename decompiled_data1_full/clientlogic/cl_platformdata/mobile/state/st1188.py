# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1188.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1188.pyc
# Source Generated with Decompyle++
# File: st1188.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func543

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 4:
        cl_action.CommonAddBagBullet(oTarget, oLifeCycle, (lambda *a: Func543(*a, **{
'dWeight': {
4502: 3333,
4503: 3333,
4504: 3334 } })), -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1189, 400, 1, { }, 0, None, None)


class CState(cl_state.CState):
    m_SID = 1188
    m_Name = '#NT#逆水行舟-扣弹'
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

