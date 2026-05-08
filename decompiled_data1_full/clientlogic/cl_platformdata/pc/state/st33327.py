# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33327.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33327.pyc
# Source Generated with Decompyle++
# File: st33327.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 0, 0, 0)
    if cl_condition.CheckSceneFightMonster(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 1070):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33328, 0, 1, { }, 1, 0, (lambda *a: Func404(*a)))
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20030):
        cl_evact.EventCBChangeStateDelayTime(oTarget, oEventCB, 0, -4000, 1)
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20031):
        cl_evact.EventCBUpdateSpreadAbnormalDam(oTarget, oEventCB, 0, 4000)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
        20030: 1 }, 1, 1, 0, 1)
    cl_evact.EventCBChangeTargetStateDelayTime(oTarget, oEventCB, 20030, 0, -4000)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
        1070: 1 }, 1, 1, 0, 1)
    cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33328, 1, 1, 0, None)
    cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DebuffFactor', 4000, 0, 0)
    cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
        20030: 1 }, 1, 1, 0, 1)
    cl_evact.EventCBChangeTargetStateDelayTime(oTarget, oEventCB, 20030, 0, -4000)


class CState(cl_state.CState):
    m_SID = 33327
    m_Name = '妖灵词条'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
    m_StartCount = 1
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
        4: CallBack4,
        5: CallBack5 }

