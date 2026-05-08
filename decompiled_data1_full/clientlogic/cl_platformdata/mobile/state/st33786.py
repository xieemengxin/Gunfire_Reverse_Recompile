# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33786.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33786.pyc
# Source Generated with Decompyle++
# File: st33786.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, TYPE_RELIFE_DICE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetRelifeAttr(oTarget, oLifeCycle, TYPE_RELIFE_DICE, 0, 0, 0, { }, 0, 99)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckRelifeTimesKey(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    cl_action.CommonSendStateStartMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeRelifTimes(oTarget, oEventCB, TYPE_RELIFE_DICE, 1)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 33786
    m_Name = '不息之力复活状态'
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

