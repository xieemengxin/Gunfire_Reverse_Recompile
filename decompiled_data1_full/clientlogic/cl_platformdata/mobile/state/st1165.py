# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1165.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1165.pyc
# Source Generated with Decompyle++
# File: st1165.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' })), 1, DAM_USE_HP)
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func403(*a, **{
'sAttr': 'ShieldMax' })), 1, DAM_USE_SHIELD)
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func403(*a, **{
'sAttr': 'ArmorMax' })), 1, DAM_USE_ARMOR)
    cl_action.CommonAddBagBullet(oTarget, oLifeCycle, 4508, 100, 0)


class CState(cl_state.CState):
    m_SID = 1165
    m_Name = '#NT#篝火交互'
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
    m_Action = (StateActAction, None)

