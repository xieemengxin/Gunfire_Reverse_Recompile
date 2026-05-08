# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33939.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33939.pyc
# Source Generated with Decompyle++
# File: st33939.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'ReloadCount', 1)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.StateSetArgValue(oTarget, oLifeCycle, 'ExtraTime', oLifeCycle.m_Owner.GetArgValue('MaxExtraTime'))


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })
    cl_action.StateAddState(oTarget, oLifeCycle, 33940, oLifeCycle.m_Owner.GetArgValue('CDTime'), {
        'DuringTime': oLifeCycle.m_Owner.GetArgValue('DuringTime'),
        'MaxExtraTime': oLifeCycle.m_Owner.GetArgValue('MaxExtraTime'),
        'MaxFloor': oLifeCycle.m_Owner.GetArgValue('MaxFloor'),
        'CDTime': oLifeCycle.m_Owner.GetArgValue('CDTime') }, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) > 0:
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, 0, 100)


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime') >= 1 and cl_evcon.CheckFromMinorPerform(oTarget, oEventCB):
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 40, 9999)
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ExtraTime', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime') - 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetWeaponPerformMaxPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD) > 0 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReloadCount') >= 1:
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oTarget, oEventCB, MAIN_HOLD, 0, 100)
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ReloadCount', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReloadCount') - 1)


def CallBack3(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime') >= 1:
        cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 40, 9999)
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ExtraTime', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraTime') - 1)


class CState(cl_state.CState):
    m_SID = 33939
    m_Name = '柳暗花明加成'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

