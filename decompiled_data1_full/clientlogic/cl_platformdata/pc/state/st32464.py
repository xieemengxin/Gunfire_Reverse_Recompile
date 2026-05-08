# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32464.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32464.pyc
# Source Generated with Decompyle++
# File: st32464.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BARRIER, WARRIOR_MONSTER
from cl_newformula import Func304

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32372):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetTargetBySummonType(oTarget, oEventCB, WARRIOR_BARRIER)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, cl_action.CommonGetSummonAttr(oTarget, oEventCB.GetCBLifeCycle(), WARRIOR_BARRIER, 'Width') / 2 + 1, WARRIOR_MONSTER, 1, 1, 0, -1, None, None, None)
    cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.5), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, 1, None, None, None, None, None, None, None)


class CState(cl_state.CState):
    m_SID = 32464
    m_Name = '#NT#弱化能流伤害效果'
    m_DieRemove = 1
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

