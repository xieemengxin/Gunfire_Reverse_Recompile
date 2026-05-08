# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1782.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1782.pyc
# Source Generated with Decompyle++
# File: st1782.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_PERFORM, EQUIP_ROCKET_LAUNCHER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if (cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM) or cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_ROCKET_LAUNCHER)) and cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 1782, 'st1782damage'):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 4000, 0, 0, '')
    elif cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_ROCKET_LAUNCHER):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 1782, 1, 'st1782damage')


class CState(cl_state.CState):
    m_SID = 1782
    m_Name = '#NT#破法子弹'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
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

