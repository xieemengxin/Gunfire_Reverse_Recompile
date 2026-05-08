# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1705.pyc
# Source Generated with Decompyle++
# File: st1705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MONSTERPF_TYPE_ATTACK, OBJ_ATTACK, OBJ_SELF, PF_TYPE_MONSTERACT, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckMonsterPFAttackType(oTarget, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 6:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 10000, 0, 0, '')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_MONSTERACT, None) and cl_evcon.CheckMonsterPFAttackType(oTarget, oEventCB, MONSTERPF_TYPE_ATTACK):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 1705
    m_Name = '#NT#六发夺命（怪物遗物）'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

