# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1316.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1316.pyc
# Source Generated with Decompyle++
# File: st1316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func217

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 1314):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', (lambda *a: Func217(*a, **{
'sAttr': 'PF-4691Head' }) * 10000), 0, None)
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', (lambda *a: Func217(*a, **{
'sAttr': 'PF-4691Head' }) * 10000), 0, None)
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', (lambda *a: Func217(*a, **{
'sAttr': 'PF-4691Head' }) * 10000), 0, None)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetSceneData(oTarget, oLifeCycle, 'PF-4691Head') == 0:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


class CState(cl_state.CState):
    m_SID = 1316
    m_Name = '#NT#每日挑战4691头目影响buff'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'firsttime': 100 }

