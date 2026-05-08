# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32883.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32883.pyc
# Source Generated with Decompyle++
# File: st32883.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, EQUIP_HANDGUN, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 9)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 32882, 0, { }, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_HANDGUN) or cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        if cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
            cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 100)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32886, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32883
    m_Name = '欲扬先抑'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        2: CallBack2 }

