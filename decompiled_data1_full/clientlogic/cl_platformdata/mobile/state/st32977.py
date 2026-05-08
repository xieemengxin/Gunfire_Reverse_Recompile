# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32977.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32977.pyc
# Source Generated with Decompyle++
# File: st32977.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func303

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckDamIsExplosion(oTarget, oEventCB):
        if cl_evcon.CheckHasState(oTarget, oEventCB, 1562):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * 3000), 0, '')
            if cl_evact.EventCBGetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes') == 0:
                cl_evact.EventCBSetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes', 1)
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                if not cl_evcon.EventCBGetTargetCustomData(oTarget, oEventCB, 'DelayedDeath') == 1:
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                    if cl_evcon.EventCBGetTargetStateRemainingTime(oTarget, oEventCB, 32004, -1) > 100:
                        cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32004, -50, 10000, 0)
                    else:
                        cl_evact.StateCBRemoveState(oTarget, oEventCB, 32004)
                else:
                    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * 2500), 0, '')
                    if cl_evact.EventCBGetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes') == 0:
                        cl_evact.EventCBSetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes', 1)
                        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                        if not cl_evcon.EventCBGetTargetCustomData(oTarget, oEventCB, 'DelayedDeath') == 1:
                            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                            if cl_evcon.EventCBGetTargetStateRemainingTime(oTarget, oEventCB, 32004, -1) > 100:
                                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32004, -50, 10000, 0)
                            else:
                                cl_evact.StateCBRemoveState(oTarget, oEventCB, 32004)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1409, 1, -1):
        if cl_evcon.CheckHasState(oTarget, oEventCB, 1562):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * 3000), 0, '')
            if cl_evact.EventCBGetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes') == 0:
                cl_evact.EventCBSetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes', 1)
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                if not cl_evcon.EventCBGetTargetCustomData(oTarget, oEventCB, 'DelayedDeath') == 1:
                    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                    if cl_evcon.EventCBGetTargetStateRemainingTime(oTarget, oEventCB, 32004, -1) > 100:
                        cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32004, -50, 10000, 0)
                    else:
                        cl_evact.StateCBRemoveState(oTarget, oEventCB, 32004)
                else:
                    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func303(*a, **{
'sAttr': 'Radius' }) * 2500), 0, '')
                    if cl_evact.EventCBGetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes') == 0:
                        cl_evact.EventCBSetCartoonUpdateValue(oTarget, oEventCB, 'pf13513_EffectTimes', 1)
                        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                        if not cl_evcon.EventCBGetTargetCustomData(oTarget, oEventCB, 'DelayedDeath') == 1:
                            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
                            if cl_evcon.EventCBGetTargetStateRemainingTime(oTarget, oEventCB, 32004, -1) > 100:
                                cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 32004, -50, 10000, 0)
                            else:
                                cl_evact.StateCBRemoveState(oTarget, oEventCB, 32004)


class CState(cl_state.CState):
    m_SID = 32977
    m_Name = '兵贵神速双持状态'
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
        1: CallBack1 }

