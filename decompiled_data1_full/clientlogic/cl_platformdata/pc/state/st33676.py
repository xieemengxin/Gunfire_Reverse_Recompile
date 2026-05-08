# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33676.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33676.pyc
# Source Generated with Decompyle++
# File: st33676.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_TYPE_CONSHOOT, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('StatusEffect'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamMul') })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamMul')), 0, 0, 1, 1)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamMul')), 0, 0, 1, 1)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack3(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamMul')), 0, 0, '')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 33676
    m_Name = '冲刺升级'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

