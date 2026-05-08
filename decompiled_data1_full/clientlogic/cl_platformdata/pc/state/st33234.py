# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33234.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33234.pyc
# Source Generated with Decompyle++
# File: st33234.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, PETPF_ACTIVE_ATTACK, PETPF_ACTIVE_SPELL, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func404, Func662

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_ADDIMMOBILIZE, -1, 1)
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_CLEARIMMOBILIZE, -1, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_ADDIMMOBILIZE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSE_CLEARIMMOBILIZE, -1, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckPerformIsPetPerformType(oTarget, oEventCB, {
        PETPF_ACTIVE_SPELL: 1,
        PETPF_ACTIVE_ATTACK: 1 }):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33235, 150, 0, { }, 0, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBRecordMasterImmobilizeMonsterNum(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ImmobilizeMonsterNum'), None)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func3(*a, **{
'a': int(Func662(*a)),
'b': 10 }))) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -6, None)
    cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func404(*a) * 500), 0, 1)


class CState(cl_state.CState):
    m_SID = 33234
    m_Name = '#NT#词条50666'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
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
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

