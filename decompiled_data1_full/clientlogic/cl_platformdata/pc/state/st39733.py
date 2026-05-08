# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39733.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39733.pyc
# Source Generated with Decompyle++
# File: st39733.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import BOX_TREBLE_DAMAGE, DAM_MASK_ELEMENT, EXTGRADE_GROUP2, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP2, 5, 0, 1)


def DelayAction(oTarget, oLifeCycle):
    oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateReceiveDam(oTarget, oLifeCycle, 500, DAM_MASK_ELEMENT, -1, -1, -1, 0, BOX_TREBLE_DAMAGE)


class CState(cl_state.CState):
    m_SID = 39733
    m_Name = '#NT#测试状态'
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
        'delay': 300,
        'firsttime': 300,
        'cnt': 1 }

