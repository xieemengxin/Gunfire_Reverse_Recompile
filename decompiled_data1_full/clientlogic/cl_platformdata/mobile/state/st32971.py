# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32971.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32971.pyc
# Source Generated with Decompyle++
# File: st32971.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateCount(oTarget, oEventCB, 32970, cl_evact.EventGetStateEffectiveCnt(oTarget, oEventCB), -1)
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1313, 'Att', 0, (lambda *a: 5000 * Func404(*a)))
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 8503, 'Att', 0, (lambda *a: 5000 * Func404(*a)))


class CState(cl_state.CState):
    m_SID = 32971
    m_Name = '#NT#刺骨飞剑2'
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
        'delay': 12,
        'firsttime': 12 }
    m_CBFuncAction = {
        0: CallBack0 }

