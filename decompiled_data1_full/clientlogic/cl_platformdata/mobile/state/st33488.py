# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33488.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33488.pyc
# Source Generated with Decompyle++
# File: st33488.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ArmorMax', -1, 1, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 80 - ((Func304(*a, **{
'sAttr': 'HPMax' }) + 99) // 100 + (Func304(*a, **{
'sAttr': 'ShieldMax' }) + 99) // 100) // 5))
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func404(*a) * 100), 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: 80 - ((Func304(*a, **{
'sAttr': 'HPMax' }) + 99) // 100 + (Func304(*a, **{
'sAttr': 'ArmorMax' }) + 99) // 100) // 5))
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func404(*a) * 100), 0, 0)


class CState(cl_state.CState):
    m_SID = 33488
    m_Name = '轻装上阵'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 80
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

