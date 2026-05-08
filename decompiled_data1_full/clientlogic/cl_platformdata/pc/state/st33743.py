# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33743.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33743.pyc
# Source Generated with Decompyle++
# File: st33743.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_CLASS, DAM_MASK_ELEMENT, FIGHT_KEY_IGNOREDEBUFF, OBJECT_OWNER, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StatusEffect'))
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'SrcLV': oLifeCycle.m_Owner.GetArgValue('GainEffect'),
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('DamReduce') })


def DelayAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('DamReduce'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetDist(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), 0, OBJECT_OWNER):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('GainEffect'), DAM_MASK_ELEMENT, '')


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, FIGHT_KEY_IGNOREDEBUFF, 0, 0, None)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func402(*a))) >= 5:
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
            cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, -oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamReduce'))
        else:
            cl_action.CommonChangeBaseReceiveDamageRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, 0)
    elif cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamReduce'), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    else:
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 0)


class CState(cl_state.CState):
    m_SID = 33743
    m_Name = '近战大师'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

