# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33457.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33457.pyc
# Source Generated with Decompyle++
# File: st33457.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: 300 * Func404(*a) + 500 * Func437(*a, **{
'sKey': 'CurCnt' })), 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CurCnt', cl_action.CommonGetMonsterStateNumInScene(oTarget, oEventCB.GetCBLifeCycle(), 'ElementMix', 100, {
        1070: 1,
        20030: 1 }))
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'Record') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurCnt'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Record', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurCnt'))
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CurCnt') }, 33457)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: 300 * Func404(*a) + 500 * Func437(*a, **{
'sKey': 'CurCnt' })), 0, 0)


class CState(cl_state.CState):
    m_SID = 33457
    m_Name = '元素步伐'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

