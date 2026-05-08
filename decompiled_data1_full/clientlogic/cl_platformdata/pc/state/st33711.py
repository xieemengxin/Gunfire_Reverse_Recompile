# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33711.pyc
# Source Generated with Decompyle++
# File: st33711.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33711 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FIGHT_KEY_WUDI, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33766, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, 1)
    cl_action.CommonForbid(oTarget, oLifeCycle, 1110)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 4)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, { })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, cl_action.CommonGetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1337, 'Radius'), WARRIOR_MONSTER, 1, 0, 0, 0, 1, 0, None)
    CustomAction(oTarget, oEventCB, {
        'MaxSize': 2 })
    cl_evact.EventCBCustomUsePerform(oTarget, oEventCB, 1337, { }, {
        'VIDList': cl_evact.EventCBGetTargeList(oTarget, oEventCB),
        'Mode': 1,
        'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()) }, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1337, 1, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Att'), 0, '')


def CallBack2(oEventCB, oTarget):
    if cl_condition.CheckInPointLevel(oTarget, oEventCB.GetCBLifeCycle(), {
        1403003: 1,
        1403004: 1,
        1101007: 1,
        7101007: 1,
        1101009: 1 }):
        cl_action.CommonSetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1337, 'Radius', 30)
    else:
        cl_action.CommonSetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1337, 'Radius', 15)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBCustomUsePerform(oTarget, oEventCB, 1337, { }, {
        'Mode': 2,
        'TransDamFactor': cl_action.StateGetSelfTransDamFactor(oTarget, oEventCB.GetCBLifeCycle()) }, 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33711
    m_Name = '#NT#迅影式'
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
    m_GameBroadcast = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 30,
        'firsttime': 30 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

