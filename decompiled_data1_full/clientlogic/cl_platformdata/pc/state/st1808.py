# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1808.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1808.pyc
# Source Generated with Decompyle++
# File: st1808.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ENEMY, OBJ_SELF, STATE_ADD_LONGORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func437, Func555

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 1808, (lambda *a: Func555(*a, **{
'sAttr': 'Att' }) * Func555(*a, **{
'sAttr': 'Trajectory' })), 'st1808damage')
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func437(*a, **{
'sKey': 'st1808damage' })))
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 1, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 8, OBJ_ENEMY, 0)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'st1808damage' }) / 100), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 0, 0, 1, 1, 1, 0, None, None, None)
    cl_evact.EventClientBehavior(oTarget, oEventCB, 1792, 0)


class CState(cl_state.CState):
    m_SID = 1808
    m_Name = '#NT#强化自爆弹夹消失效果'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 40
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

