# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7970.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7970.pyc
# Source Generated with Decompyle++
# File: st7970.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 7973, 0)
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonForbid(oTarget, oLifeCycle, 1038)
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 4201, 1, None, None)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveSelf(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 7973, 0, { }, None)


class CState(cl_state.CState):
    m_SID = 7970
    m_Name = '#NT#小触手召唤物休眠'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 2000,
        'cnt': 1 }

