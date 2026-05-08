# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32774.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32774.pyc
# Source Generated with Decompyle++
# File: st32774.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_SKILL_DURATION_BEGIN, MAIN_SKILL_DURATION_END, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)
    cl_action.CommonForbid(oTarget, oLifeCycle, 1064)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_BEGIN, {
        'StateSID': 32774 })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, None, None)
    cl_action.CommonSubPointPerformColdTime(oTarget, oLifeCycle, 1310, 0, 100)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StatePerformAddColdTime(oTarget, oLifeCycle)
    cl_action.StateAddState(oTarget, oLifeCycle, 32802, 70, { }, None)
    cl_action.CommonSendMessage(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_SKILL_DURATION, MAIN_SKILL_DURATION_END, {
        'StateSID': 32774 })
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, None, None)
    cl_action.StateAddState(oTarget, oLifeCycle, 32804, 43, { }, None)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32814, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None) == False:
        if cl_evcon.CheckSourceInSelfFace(oTarget, oEventCB, 75, {
            31262: 1,
            39091: 1,
            39012: 1,
            39013: 1,
            21221: 1,
            21223: 1,
            21282: 1,
            23815: 1,
            30011: 1,
            31255: 1,
            31263: 1,
            32423: 1,
            32811: 1,
            39211: 1,
            33811: 1,
            39250: 1,
            39093: 1 }, {
            23815: 2,
            30011: 2,
            21221: 2,
            33812: 2 }) or cl_evcon.CheckTargetPointBaseSummon(oTarget, oEventCB, 1028):
            CustomAction(oTarget, oEventCB, {
                'MsgType': 'block' })
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'MsgType': 'hold' })


def CallBack3(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'MsgType': 'receive' })


class CState(cl_state.CState):
    m_SID = 32774
    m_Name = '#NT#钢铁之盾'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3 }


def CustomAction(oTarget, oEventCB, dArgs):
    sType = dArgs['MsgType']
    if sType == 'hold':
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHIELD_HOLD, oTarget, { })
    elif sType == 'block':
        dMsgInfo = oEventCB.GetCBMsgInfo()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHIELD_BLOCK, oTarget, dMsgInfo)
    elif sType == 'receive':
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, oTarget, { })

