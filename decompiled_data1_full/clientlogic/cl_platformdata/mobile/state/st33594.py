# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33594.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33594.pyc
# Source Generated with Decompyle++
# File: st33594.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func706

def StateActAction(oTarget, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 1:
        cl_action.CommonSetEventNpcInteract(oTarget, oLifeCycle, 0)
        cl_action.CommonSetAllRelicUnRemove(oTarget, oLifeCycle)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE, -1, 2, 0, 0)
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 6)
    if oLifeCycle.m_Owner.GetArgValue('StatusEffect') == 2:
        cl_action.CommonSetEventNpcInteract(oTarget, oLifeCycle, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeRelicValidRemove(oTarget, oEventCB, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func706(*a))) != -1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) <= 0:
            cl_evact.EventCBRemoveRelic(oTarget, oEventCB, 5841, 1)


class CState(cl_state.CState):
    m_SID = 33594
    m_Name = '来者不拒'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2 }

