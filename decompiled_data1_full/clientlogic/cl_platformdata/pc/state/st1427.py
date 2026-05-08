# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1427.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1427.pyc
# Source Generated with Decompyle++
# File: st1427.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1471, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1427, 1, 1, None, None)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0 and cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13022):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 5000 + 0), DAM_TYPE_WEAPON, '')
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1471, 0, { }, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 13022) and cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 1471):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1471, 1)


class CState(cl_state.CState):
    m_SID = 1427
    m_Name = '#NT#13022-监听击杀'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
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
        1: CallBack1,
        2: CallBack2 }

