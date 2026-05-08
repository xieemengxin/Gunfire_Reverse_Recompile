# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33100.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33100.pyc
# Source Generated with Decompyle++
# File: st33100.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33100 as CustomAction
import cl_state
from cl_commondefines import ENTER_INKAREA, LEAVE_INKAREA, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_COUNT_MAX, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeStateAttr(oTarget, oLifeCycle, 0, oLifeCycle.m_Owner.GetArgValue('MaxCount'), STATE_COUNT_MAX, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, LEAVE_INKAREA, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, ENTER_INKAREA, 6, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 1)
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 7)
    cl_action.CommonListenLevelCtrlMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 2)


def DelayAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'CostLevel': 1,
        'TriggerCount': (lambda *a: Func402(*a) + 2) })


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'Leave': 1,
        'HeroStateTime': 0 })
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckVirtualArea(oTarget, oEventCB) == 0 and cl_condition.CheckSceneFightMonster(oTarget, oEventCB.GetCBLifeCycle()):
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Enter': 1,
            'HeroStateTime': 0 })


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0 and cl_evcon.CheckTargetInInkArea(oTarget, oEventCB) == 0:
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Enter': 1,
            'HeroStateTime': 0 })
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 4)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.EventCBCheckSameScene(oTarget, oEventCB):
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Leave': 1,
            'HeroStateTime': 0 })


def CallBack6(oEventCB, oTarget):
    if not cl_evcon.EventCBCheckVirtualArea(oTarget, oEventCB):
        cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 0, 33100, 'InVirtual')


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER) and cl_evcon.EventCBCheckLevelGoal(oTarget, oEventCB) and cl_evcon.GetSceneMonsterCnt(oTarget, oEventCB, 1) == 0:
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Leave': 1,
            'HeroStateTime': 0 })


class CState(cl_state.CState):
    m_SID = 33100
    m_Name = '浴墨蚀心'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        6: CallBack6,
        7: CallBack7 }

