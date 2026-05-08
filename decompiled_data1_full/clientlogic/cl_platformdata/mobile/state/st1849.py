# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1849.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1849.pyc
# Source Generated with Decompyle++
# File: st1849.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_CLASS, DAM_MASK_ELEMENT, ITEM_MODE_DRILLFOCUS, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 4000, 0, -1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, 5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.ImmunitySubSpdStateByMonster(oTarget, oLifeCycle)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9606, 0, 1):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 4000, 0, '')


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.EventCBCheckWeaponModeByHoldType(oTarget, oEventCB, 0, ITEM_MODE_DRILLFOCUS):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1849
    m_Name = '钻头'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 65
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

