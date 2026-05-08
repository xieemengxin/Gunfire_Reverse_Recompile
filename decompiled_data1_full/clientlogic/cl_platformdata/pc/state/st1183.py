# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1183.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1183.pyc
# Source Generated with Decompyle++
# File: st1183.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WEAPON_MAIN_PERFORM

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 18)
    cl_action.CommonTriggerWeaponPerformBehavior(oTarget, oLifeCycle, WEAPON_MAIN_PERFORM, 2014, 0, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerWeaponPerformBehavior(oTarget, oLifeCycle, WEAPON_MAIN_PERFORM, 2014, 1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


class CState(cl_state.CState):
    m_SID = 1183
    m_Name = '#NT#铭刻4876'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (None, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

