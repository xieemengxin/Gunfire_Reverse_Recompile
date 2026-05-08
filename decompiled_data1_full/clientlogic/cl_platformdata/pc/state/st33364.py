# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33364.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33364.pyc
# Source Generated with Decompyle++
# File: st33364.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, SMITHNPCSUBMSG_UPGRADE, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5957) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, '33364Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, 1, '33364Enable')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 3, 0, 0)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, '33364Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, 0, '33364Enable')
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE)


def CallBack1(oEventCB, oTarget):
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, '33364Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, 1, '33364Enable')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 3, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, '33364Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33364, 0, '33364Enable')
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE)


def CallBack3(oEventCB, oTarget):
    cl_evact.CBTriggerGroup(oTarget, oEventCB, {
        4: 1500 }, 1)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBAddWeaponUpgradeLevel(oTarget, oEventCB, -1)
    cl_evact.EventCBWeaponClientBehavior(oTarget, oEventCB, 61021, 0)


class CState(cl_state.CState):
    m_SID = 33364
    m_Name = '火候欠缺'
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

