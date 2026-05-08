# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33365.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33365.pyc
# Source Generated with Decompyle++
# File: st33365.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5958) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33365, '33365Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33365, 1, '33365Enable')
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', -5000, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', -5000, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, 3000, 1)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33365, '33365Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33365, 0, '33365Enable')
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, 0, 1)


class CState(cl_state.CState):
    m_SID = 33365
    m_Name = '破旧衣物'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

