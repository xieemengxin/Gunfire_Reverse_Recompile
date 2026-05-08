# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33097.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33097.pyc
# Source Generated with Decompyle++
# File: st33097.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_LONG, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func14, Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func361(*a, **{
'sid': 1431,
'sArgs': 'MoveSpeed_Buff' })), 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 1325,
'sArgs': 'ShieldRecoverAdd' })), 0, DAM_USE_SHIELD)
    cl_action.CommonModifyInkValue(oTarget, oLifeCycle, 2, 'From33097', { })


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 33314, 100, { }, None)


def CallBack0(oEventCB, oTarget):
    if cl_evact.EventCBGetCustomData(oTarget, oEventCB, '33097_Next') > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func14(*a))) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: cl_evact.EventCBGetCustomData(oTarget, oEventCB, '33097_Next') - Func14(*a))) < 25:
        cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: (cl_evact.EventCBGetCustomData(oTarget, oEventCB, '33097_Next') - Func14(*a)) * 4), 100, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evact.EventCBGetCustomData(oTarget, oEventCB, '33097_Next') <= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func14(*a))):
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, '33097_Next', (lambda *a: Func14(*a) + 25))


class CState(cl_state.CState):
    m_SID = 33097
    m_Name = '清域'
    m_DieRemove = 1
    m_DyingRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONG
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

