# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1790.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1790.pyc
# Source Generated with Decompyle++
# File: st1790.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_FRIEND_HERO, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func304, Func374

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: min(int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 50 / 100), int(Func374(*a) - 2))), DAM_TYPE_TRUE, 0, 0, 0, 0, None)
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 15, OBJ_FRIEND_HERO, 0)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) == 1:
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 1790, -1, 0, 0, None)
    else:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1790
    m_Name = '独木难支'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 15
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

