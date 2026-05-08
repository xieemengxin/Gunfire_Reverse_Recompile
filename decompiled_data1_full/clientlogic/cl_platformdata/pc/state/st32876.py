# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32876.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32876.pyc
# Source Generated with Decompyle++
# File: st32876.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, EQUIP_HANDGUN, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 6)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 5000, 0, DAM_TYPE_WEAPON, '')
        if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
            if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_HANDGUN) or cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
                cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            
        if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        elif cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
            if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_HANDGUN) or cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
                cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            elif cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0 and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


def CallBack4(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 5000, 0, DAM_TYPE_PERFORM, '')


class CState(cl_state.CState):
    m_SID = 32876
    m_Name = '烛微洞幽'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        4: CallBack4 }

