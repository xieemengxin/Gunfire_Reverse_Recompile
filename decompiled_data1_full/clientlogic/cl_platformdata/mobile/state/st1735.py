# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1735.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1735.pyc
# Source Generated with Decompyle++
# File: st1735.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, OBJ_SELF, OBJ_VICTIM, SKILLCACHE_INT, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 18)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None):
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 100)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: Func404(*a) * 3000 + 0), DAM_TYPE_WEAPON, '')
        if cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT):
            cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 25, 500)
        elif cl_evcon.StateCheckFromSameAttacker(oTarget, oEventCB, None, None) and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: Func404(*a) * 3000 + 0), DAM_TYPE_WEAPON, '')
            if cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT):
                cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 25, 500)


class CState(cl_state.CState):
    m_SID = 1735
    m_Name = '机瞄步枪13050虚弱'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

