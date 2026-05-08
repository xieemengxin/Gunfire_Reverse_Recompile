# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8155.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8155.pyc
# Source Generated with Decompyle++
# File: st8155.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction8155_0 as CustomAction0, CustomAction8155_1 as CustomAction1
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 0, 1)
    CustomAction0(oTarget, oLifeCycle, {
        'Radius': (lambda *a: Func429(*a, **{
'sArg': 'LockRadius' })),
        'High': (lambda *a: Func429(*a, **{
'sArg': 'LockRadius' })) })


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction1(oTarget, oLifeCycle, { })
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 0, { })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateStartMessage(oTarget, oLifeCycle, 0, 1)


class CState(cl_state.CState):
    m_SID = 8155
    m_Name = '#NT#普通缚影印'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
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
    m_Action = (StateActAction, StateRemoveAction)
    m_RefreshFunc = {
        'action': StateRefreshAction }

