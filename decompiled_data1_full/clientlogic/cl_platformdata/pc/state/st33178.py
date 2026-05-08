# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33178.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33178.pyc
# Source Generated with Decompyle++
# File: st33178.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)


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
            cl_evact.EventCBHaltFlow(oTarget, oEventCB)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
            if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) == 1:
                cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), 500, 0)
                cl_action.CommonSendMessage(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PARRY, -1, { })


class CState(cl_state.CState):
    m_SID = 33178
    m_Name = '#NT#狮子蓄力冲拳格挡伤害'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

