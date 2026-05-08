# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33058.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33058.pyc
# Source Generated with Decompyle++
# File: st33058.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DIE_PRIORITY_PF_NO_DIE, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func407, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetDiePriority(oTarget, oLifeCycle, DIE_PRIORITY_PF_NO_DIE)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 100)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'TransDam' }))):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveAllStateByType(oTarget, oLifeCycle, STATE_CLS_ABNORMAL)
    cl_action.StateAddState(oTarget, oLifeCycle, 33060, 200, { }, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: -Func361(*a, **{
'sid': 1325,
'sArgs': 'DamReduceRatio' })), 0, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBAddTargetStateTime(oTarget, oEventCB, 33044, -200, (lambda *a: Func407(*a, **{
'sid': 33044 })))
    cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeHP(oTarget, oEventCB, 100)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1326, 1, 0):
        cl_evact.StateCBChangeSkillDamFactorBySelfTransDamFactor(oTarget, oEventCB)
        cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, 'ParentActNum', (lambda *a: Func429(*a, **{
'sArg': 'ParentActNum' })))


class CState(cl_state.CState):
    m_SID = 33058
    m_Name = '#NT#墨灵出击期间效果'
    m_DieRemove = 1
    m_DyingRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

