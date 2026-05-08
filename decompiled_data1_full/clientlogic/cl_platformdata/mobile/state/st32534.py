# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32534.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32534.pyc
# Source Generated with Decompyle++
# File: st32534.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FLOWER_DAMAGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func360

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
        if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8004, 1, None) == 0 or cl_evcon.CheckTriggerPerfromPfid(oTarget, oEventCB, {
            0: 1313 }):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32500, 0, 1, None, None):
                cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32500, (lambda *a: 1 + Func336(*a, **{
'sKey': '1313-Curtimes' })), 1, 0, None)
                if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32500, 1, None) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func360(*a, **{
'sid': 8004,
'sAttr': 'DamInterval' }))):
                    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32500, -cl_action.CommonGetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 8004, 'DamInterval'), 1, None, None)
                    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 8004, {
                        'HitTimes': 1,
                        'DamageMul': 100 }, None)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8004, 1, None):
        cl_evact.EventCBSetDamShowTipsType(oTarget, oEventCB, FLOWER_DAMAGE)


class CState(cl_state.CState):
    m_SID = 32534
    m_Name = '#NT#媚影伤害'
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
        5: CallBack5 }

