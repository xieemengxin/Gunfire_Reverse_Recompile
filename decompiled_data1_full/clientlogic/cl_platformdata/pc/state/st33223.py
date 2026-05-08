# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33223.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33223.pyc
# Source Generated with Decompyle++
# File: st33223.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import HATEMETHOD_ACCESSIBLE, OBJ_SELF, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 6, 1, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBGetLockEnemy(oTarget, oEventCB, 0, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_ACCESSIBLE, {
        'Range': 20 })
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3333,
            3: 3334,
            4: 3335 }, 1)
    if cl_condition.StateCheckUsedUpDelayCnt(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB):
        cl_evact.CBTriggerGroup(oTarget, oEventCB, {
            2: 3333,
            3: 3334,
            4: 3335 }, 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 7326, { }, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 7327, { }, None)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 7328, { }, None)


def CallBack5(oEventCB, oTarget):
    if cl_condition.StateCheckUsedUpDelayCnt(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33223
    m_Name = '#NT#词条50538召唤法球'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 2
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 30,
        'cnt': 6 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

