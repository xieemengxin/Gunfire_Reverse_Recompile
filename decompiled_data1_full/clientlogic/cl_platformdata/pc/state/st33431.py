# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33431.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33431.pyc
# Source Generated with Decompyle++
# File: st33431.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_LASER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func304, Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'Energy', -1, 11, 0, 0)
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 32709)
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 1522)


def CallBack0(oEventCB, oTarget):
    if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32661) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
                cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func331(*a, **{
'sid': 3107 }) * (Func331(*a, **{
'sid': 3107 }) + 4) * 10))
            else:
                cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'pf3107', 1, None)
            cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -1000 * Func331(*a, **{
'sid': 3107 })), 0)


def CallBack11(oEventCB, oTarget):
    if oTarget.Energy() < cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.5)):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33431
    m_Name = '#NT#燃烧子弹无CD效果'
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
        11: CallBack11 }

