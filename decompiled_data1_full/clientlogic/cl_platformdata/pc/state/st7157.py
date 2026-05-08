# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7157.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7157.pyc
# Source Generated with Decompyle++
# File: st7157.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction7157 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func589

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonPauseMonsterOwnerAgent(oTarget, oLifeCycle)
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'ShieldMax', (lambda *a: Func589(*a)))
    CustomAction(oTarget, oLifeCycle, {
        'Perform': {
            39068: 1,
            39057: 3 },
        'WaitPerform': {
            39054: 1 } })


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonClearForceAttr(oTarget, oLifeCycle, 'ShieldMax')


class CState(cl_state.CState):
    m_SID = 7157
    m_Name = '#NT#轮回10夜姬丸7阶段表演'
    m_DieRemove = 1
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
    m_Action = (StateActAction, StateRemoveAction)

