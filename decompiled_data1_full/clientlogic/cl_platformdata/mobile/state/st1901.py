# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1901.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1901.pyc
# Source Generated with Decompyle++
# File: st1901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437, Func686

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetWeaponPFBulletNum(oTarget, oLifeCycle, 9793) > cl_condition.StateCheckStatistics(oTarget, oLifeCycle, 'Cost'):
        cl_action.StateAddFromSkillCollectInfo(oTarget, oLifeCycle, 'EnergyCost', (lambda *a: Func437(*a, **{
'sKey': 'Cost' })), 0)
        cl_action.CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, 9793, (lambda *a: Func437(*a, **{
'sKey': 'Cost' })))
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    else:
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 9793)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1900, 0)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1901, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Cost', (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletUse' })))


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'Cost' }) * 2.5 / 100), 'Cost')


class CState(cl_state.CState):
    m_SID = 1901
    m_Name = '#NT#浮游炮-铭刻能量消耗'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

