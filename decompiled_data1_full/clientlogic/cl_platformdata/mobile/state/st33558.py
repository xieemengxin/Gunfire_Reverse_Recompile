# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33558.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33558.pyc
# Source Generated with Decompyle++
# File: st33558.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Dam'), 0, DAM_MASK_ELEMENT, 1, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Dam'), 0, DAM_MASK_ELEMENT, '')


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Dam'), DAM_MASK_ELEMENT, 1, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Dam'), 0, DAM_MASK_ELEMENT, '')


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBSetWandCount(oTarget, oEventCB, (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'DamAdd' }) // 100))


class CState(cl_state.CState):
    m_SID = 33558
    m_Name = '#NT#隐身法杖隐身状态后增伤状态'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

