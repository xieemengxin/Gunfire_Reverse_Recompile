# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32756.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32756.pyc
# Source Generated with Decompyle++
# File: st32756.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_item.defines import MAIN_HOLD
from cl_newformula import Func404

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) < 1:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', (lambda *a: Func404(*a) * 5000), 0, MAIN_HOLD)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', (lambda *a: Func404(*a) * 5000), 0, -1)


class CState(statedata.CStateData):
    m_SID = 32756
    m_Name = '全力一押'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }

