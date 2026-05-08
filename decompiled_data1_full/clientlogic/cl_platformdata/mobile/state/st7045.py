# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7045.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7045.pyc
# Source Generated with Decompyle++
# File: st7045.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DOUBLE_SHOOT_SETTLE_DAMAGE, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'OriginID': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cache') })
    cl_evact.EventTargetDamage(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_TYPE_NORMAL | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 1, 0, 0, 1, 0, 0, 0, 0, DOUBLE_SHOOT_SETTLE_DAMAGE, 0, None)


class CState(cl_state.CState):
    m_SID = 7045
    m_Name = '#NT#双发步枪停滞状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

