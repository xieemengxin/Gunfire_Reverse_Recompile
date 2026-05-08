# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33354.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33354.pyc
# Source Generated with Decompyle++
# File: st33354.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func379

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDoneEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5946) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33354, '33354Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33354, 1, '33354Enable')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 3, 0, 0)
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -(25 * Func379(*a))), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33354, '33354Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33354, 0, '33354Enable')
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_HP_CHANGE, -1)
        cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonModifyDamResistance(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -(25 * Func379(*a))), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CState(cl_state.CState):
    m_SID = 33354
    m_Name = '脆弱之躯'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

