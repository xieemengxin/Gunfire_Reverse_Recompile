# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1461.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1461.pyc
# Source Generated with Decompyle++
# File: st1461.pyc (Python 3.6)

from cl_platformdata.custom.state.customaction import CustomAction1461 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_SERVANT, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 1:
        cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 1701, 0, None, None)
    else:
        cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1701)


def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 1:
        cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 1701)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameAttacker(oTarget, oEventCB, 1, OBJECT_SERVANT) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 1 and cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 4)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'OnArea'):
            CustomAction(oTarget, oEventCB, {
                'Perform': 12026 })
        else:
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            CustomAction(oTarget, oEventCB, {
                'Perform': 12026 })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameAttacker(oTarget, oEventCB, 0, 0) and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        9701: 1,
        9792: 1 }, 0, 0):
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 1 or cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 4)
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'OnArea'):
                CustomAction(oTarget, oEventCB, {
                    'Perform': 12026 })
            else:
                cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
                CustomAction(oTarget, oEventCB, {
                    'Perform': 12026 })
        else:
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


class CState(cl_state.CState):
    m_SID = 1461
    m_Name = '#NT#标记法杖标记'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

