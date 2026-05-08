# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33190.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33190.pyc
# Source Generated with Decompyle++
# File: st33190.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 3)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 5000, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'AttSpeed', -5000, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBHaltFlow(oTarget, oEventCB)
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'RHP', -10000, 0, 0)
    cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: 100 - Func304(*a, **{
'sAttr': 'HP' })))
    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1445, 0, { }, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1445, 0)
    cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 20000, 0, 0, '')


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckAssistKill(oTarget, oEventCB):
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 800, 800)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckTargetPetPointBaseMonster(oTarget, oEventCB, 2221):
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33190
    m_Name = '#NT#词条50521'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

