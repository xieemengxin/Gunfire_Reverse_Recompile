# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1812.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1812.pyc
# Source Generated with Decompyle++
# File: st1812.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, OBJ_SELF, OBJ_VICTIM, SKILLCACHE_INT, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func413

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1730, 0, 1, 0, None) and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0 and cl_evcon.CheckFromWeapon(oTarget, oEventCB, 1):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: Func413(*a, **{
'iState': 1730 }) * 3000 * (30 - Func413(*a, **{
'iState': 1730 })) / (20 + Func413(*a, **{
'iState': 1730 })) + 0), DAM_TYPE_WEAPON, '')
        if cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT):
            cl_evact.StateCBAddTargetStateTime(oTarget, oEventCB, 1730, 25, 1000, 1)
            cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 25, 1000)
            if cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13050) and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1730, 0, 1, 0, 0) and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
                cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 80)
            elif cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13050) and cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1730, 0, 1, 0, 0) and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
                cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 80)


class CState(cl_state.CState):
    m_SID = 1812
    m_Name = '#NT#机瞄步枪（玩家）'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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

