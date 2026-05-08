# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1900.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1900.pyc
# Source Generated with Decompyle++
# File: st1900.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func686

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDisableWeaponPerform(oTarget, oLifeCycle, 4386)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9793) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletUse' }))):
        cl_action.StateAddFromSkillCollectInfo(oTarget, oLifeCycle, 'EnergyCost', (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletUse' })), 0)
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletUse' })))
    else:
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 9793)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1901, 0)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1900, 0)


class CState(cl_state.CState):
    m_SID = 1900
    m_Name = '#NT#浮游炮-能量消耗'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 8,
        'firsttime': 8 }

