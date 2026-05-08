# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33096.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33096.pyc
# Source Generated with Decompyle++
# File: st33096.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 33103, 0, { }, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDeviceUsePF(oTarget, oLifeCycle, 7201, { })


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33103, 0)
    cl_action.CommonSetDeciveAcitveStatus(oTarget, oLifeCycle, 0)


class CState(cl_state.CState):
    m_SID = 33096
    m_Name = '#NT#屏障装置-携带组件'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 1000 }

