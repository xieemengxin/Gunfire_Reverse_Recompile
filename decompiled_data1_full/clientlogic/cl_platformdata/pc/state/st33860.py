# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33860.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33860.pyc
# Source Generated with Decompyle++
# File: st33860.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_COUNT_MAX, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeStateAttr(oTarget, oLifeCycle, 0, oLifeCycle.m_Owner.GetArgValue('MaxCount'), STATE_COUNT_MAX, 1)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33860, oLifeCycle.m_Owner.GetArgValue('MaxAttrAdd'), 'MaxAttrAdd')


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33860, cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33860, 'MaxAttrAdd'), 0)
    if cl_evcon.CheckHasState(oTarget, oEventCB, 33604):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func404(*a) * 100), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func404(*a) * 100), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func404(*a) * 100), 0)


class CState(cl_state.CState):
    m_SID = 33860
    m_Name = '愈战愈勇'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0 }

