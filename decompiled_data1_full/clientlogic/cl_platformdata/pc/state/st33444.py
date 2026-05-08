# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33444.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33444.pyc
# Source Generated with Decompyle++
# File: st33444.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CanTrigger') and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1960: 1 }, 1, 0) == 0:
        cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 0, 33444, 'CanTrigger')
        cl_evact.DelayTriggerGroup(oTarget, oEventCB, 2, 1, 300, 0, 0, { })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33436, 200, 0, { }, 1, 0, None)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1960, {
            '33444Trigger': 1 }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, '33444Trigger') and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1960: 1 }, 1, 0):
        cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, 0, None, None, None, None)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1960, { }, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 1, 33444, 'CanTrigger')


class CState(cl_state.CState):
    m_SID = 33444
    m_Name = '风行草偃2级效果'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

