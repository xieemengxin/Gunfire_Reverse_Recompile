# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33858.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33858.pyc
# Source Generated with Decompyle++
# File: st33858.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    if oLifeCycle.m_Owner.GetArgValue('SpeedRatio') > 0:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func404(*a) * oLifeCycle.m_Owner.GetArgValue('SpeedRatio')), 0, -1)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func404(*a) * oLifeCycle.m_Owner.GetArgValue('SpeedRatio')) })


def StateCountAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('SpeedRatio') > 0:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func404(*a) * oLifeCycle.m_Owner.GetArgValue('SpeedRatio')), 0, -1)
        cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
            'ExcessiveDam': (lambda *a: Func404(*a) * oLifeCycle.m_Owner.GetArgValue('SpeedRatio')) })


class CState(cl_state.CState):
    m_SID = 33858
    m_Name = '灵气护体'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }

