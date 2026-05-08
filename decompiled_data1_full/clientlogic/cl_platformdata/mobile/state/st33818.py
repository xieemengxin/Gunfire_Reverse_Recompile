# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33818.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33818.pyc
# Source Generated with Decompyle++
# File: st33818.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_HP, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'IntervalTime' })), (lambda *a: Func429(*a, **{
'sArg': 'IntervalTime' })), 0)
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxHpEffect'))
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, 0)


def DelayAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('HPMaxAdd'):
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'RecoverHP' }) * 100), 0, DAM_USE_HP)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('HPMaxAdd'), None)
    else:
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'RecoverHP' }) * 100), 0, DAM_USE_HP)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', 0, (lambda *a: Func404(*a) * 100), 0)


class CState(cl_state.CState):
    m_SID = 33818
    m_Name = '血契魔法'
    m_IsShow = 1
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
        'delay': 300,
        'firsttime': 300 }
    m_CountFunc = {
        'action': StateCountAction }

