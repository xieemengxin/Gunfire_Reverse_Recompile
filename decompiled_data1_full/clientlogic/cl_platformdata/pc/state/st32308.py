# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32308.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32308.pyc
# Source Generated with Decompyle++
# File: st32308.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func354, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1414, 0, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 15000, DAM_TYPE_PERFORM, '')
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2408) == 3:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32346 }) / 2), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, 1, None, None, None, None, None, None, None)
            cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32346, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
        cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 32308)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1414, 0, None):
        if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2408) >= 2:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32345, 10, 0, {
                'ExcessChange': (lambda *a: Func354(*a)) }, 0, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
            cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 32308)


class CState(cl_state.CState):
    m_SID = 32308
    m_Name = '#NT#首当其冲'
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
        1: CallBack1,
        3: CallBack3,
        4: CallBack4 }

