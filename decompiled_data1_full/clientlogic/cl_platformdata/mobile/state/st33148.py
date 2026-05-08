# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33148.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33148.pyc
# Source Generated with Decompyle++
# File: st33148.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenDeviceMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonChangeDeviceEnergy(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('Att'), 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamReduce'), DAM_MASK_ELEMENT, '')


class CState(cl_state.CState):
    m_SID = 33148
    m_Name = '#NT#炮台50123伤害削减'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

