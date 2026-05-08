# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8169.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8169.pyc
# Source Generated with Decompyle++
# File: st8169.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction8169_0 as CustomAction0, CustomAction8169_1 as CustomAction1
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': oLifeCycle.m_Owner.GetArgValue('LimitMoveSummon') })
    CustomAction0(oTarget, oLifeCycle, { })


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction1(oTarget, oLifeCycle, { })


class CState(cl_state.CState):
    m_SID = 8169
    m_Name = '#NT#天袭束缚状态'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_SPECIAL
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
    m_Action = (StateActAction, StateRemoveAction)

