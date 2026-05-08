# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33394.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33394.pyc
# Source Generated with Decompyle++
# File: st33394.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func589

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func589(*a) * 0.1), 33373, 'MagicShieldCurValue')
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func589(*a) * 0.1), 33373, 'MagicShieldMaxValue')
    cl_action.CommonTriggerStateRefreshBehavior(oTarget, oEventCB.GetCBLifeCycle(), 33373, { }, None, None)


class CState(cl_state.CState):
    m_SID = 33394
    m_Name = '#NT#怪物遗物法术护盾延迟回复'
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
        'delay': 5,
        'firsttime': 500,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

