# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33679.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33679.pyc
# Source Generated with Decompyle++
# File: st33679.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'DebuffFactor', oLifeCycle.m_Owner.GetArgValue('GainEffect'), 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 1070):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33675, 0, 1, {
            'AdditionDam': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbnormalSourceDam') }, 0, 0, None)
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20030):
        cl_evact.EventCBChangeStateDelayTime(oTarget, oEventCB, 0, -oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbnormalSourceDam'), 1)
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20031):
        cl_evact.EventCBUpdateSpreadAbnormalDam(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbnormalSourceDam'))


def CallBack3(oEventCB, oTarget):
    if cl_condition.CheckSceneFightMonster(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
            1070: 1 }, 1, 1, 0, 1)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33675, 0, 1, {
            'AdditionDam': oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbnormalSourceDam') }, 0, 0, None)
        cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
            20030: 1 }, 1, 1, 0, 1)
        cl_evact.EventCBChangeTargetStateDelayTime(oTarget, oEventCB, 20030, 0, -oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AbnormalSourceDam'))


class CState(cl_state.CState):
    m_SID = 33679
    m_Name = '元素专精骰子词条'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

