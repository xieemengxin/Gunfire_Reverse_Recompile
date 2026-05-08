# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1522.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1522.pyc
# Source Generated with Decompyle++
# File: st1522.pyc (Python 3.6)

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


def CallBack0(oEventCB, oTarget):
    if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32661) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER):
            if oTarget.Energy() >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 0.5 * Func304(*a, **{
'sAttr': 'EnergyMax' }))):
                if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
                    cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 10 + Func331(*a, **{
'sid': 3107 }) * 20))
                else:
                    cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'pf3107', 1, None)
                cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -400 - Func331(*a, **{
'sid': 3107 }) * 200), 0)
            elif not cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()):
                cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 500)
                cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 500 + 1000 * Func331(*a, **{
'sid': 3107 })), 0)


class CState(cl_state.CState):
    m_SID = 1522
    m_Name = '#NT#燃烧子弹'
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
        0: CallBack0 }

