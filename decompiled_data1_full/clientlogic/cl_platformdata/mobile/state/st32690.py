# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32690.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32690.pyc
# Source Generated with Decompyle++
# File: st32690.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BUILD_TRAP
from cl_newformula import Func305, Func311, Func312, Func313

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 12)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, None) and cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32625) == 0:
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) + Func312(*a) + Func313(*a) - 100))
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32625, 12000, { }, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32691, 100, { }, None)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 5, 1, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 6, 1, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY) and not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BUILD_TRAP):
            cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8505, {
                'chopsTimes': 1,
                'Att': 200 }, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8505, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeShield(oTarget, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ShieldMax' }) + 0))
        cl_evact.EventChangeArmor(oTarget, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'ArmorMax' }) + 0))
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF)


def CallBack6(oEventCB, oTarget):
    cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF)


class CState(cl_state.CState):
    m_SID = 32690
    m_Name = '#NT#方寸不乱'
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
        5: CallBack5,
        6: CallBack6 }

