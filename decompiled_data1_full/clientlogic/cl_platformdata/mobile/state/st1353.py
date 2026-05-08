# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1353.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1353.pyc
# Source Generated with Decompyle++
# File: st1353.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetShieldRatio(oTarget, oEventCB) == 100 or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: max(0, Func304(*a, **{
'sAttr': 'ArmorMax' }) - 100))):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 2500, 0, 0, '')


class CState(cl_state.CState):
    m_SID = 1353
    m_Name = '#NT#【强化】虚张声势'
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
        0: CallBack0 }

