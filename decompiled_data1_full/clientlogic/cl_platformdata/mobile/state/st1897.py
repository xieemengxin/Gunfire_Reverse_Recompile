# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1897.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1897.pyc
# Source Generated with Decompyle++
# File: st1897.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func686

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9093) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func686(*a, **{
'iPerform': 9093,
'sAttr': 'PFBulletUse' }))):
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9093, (lambda *a: Func686(*a, **{
'iPerform': 9093,
'sAttr': 'PFBulletUse' })))
    else:
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 9093)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1897, 0)


class CState(cl_state.CState):
    m_SID = 1897
    m_Name = '#NT#追踪步枪能量消耗'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 24 }

