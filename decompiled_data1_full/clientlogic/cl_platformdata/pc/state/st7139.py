# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7139.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7139.pyc
# Source Generated with Decompyle++
# File: st7139.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import NWARRIOR_NPC_CANNON, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func235

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_NPCINTERACT, -1, 2)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3, 0, 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckNPCType(oTarget, oEventCB, NWARRIOR_NPC_CANNON):
        cl_evact.EventCBKillMonsterGroup(oTarget, oEventCB, 99)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1697: 10,
        39067: 10 }, 1, 0):
        cl_evact.EventCBKillMonsterGroup(oTarget, oEventCB, 99)
        cl_evact.EventCBAppointSummonAreaMonster(oTarget, oEventCB, 99, {
            5: 10,
            10: 10,
            11: 10,
            12: 10 }, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' })), 0, 0, 1)
        cl_evact.EventCBAppointSummonAreaMonster(oTarget, oEventCB, 99, {
            6: 10,
            13: 10,
            14: 10,
            15: 10 }, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' })), 0, 0, 1)
        cl_evact.EventCBRemoveMonsterGroupReward(oTarget, oEventCB, 99, 1)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 39065, 1, 0):
        if cl_evcon.CheckMonsterPhase(oTarget, oEventCB, 2) or cl_evcon.CheckMonsterPhase(oTarget, oEventCB, 4) or cl_evcon.CheckMonsterPhase(oTarget, oEventCB, 6):
            cl_evact.EventCBKillMonsterGroup(oTarget, oEventCB, 99)
            cl_evact.EventCBAppointSummonAreaMonster(oTarget, oEventCB, 99, {
                5: 10,
                10: 10,
                11: 10,
                12: 10 }, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' })), 0, 0, 1)
            cl_evact.EventCBAppointSummonAreaMonster(oTarget, oEventCB, 99, {
                6: 10,
                13: 10,
                14: 10,
                15: 10 }, (lambda *a: Func235(*a, **{
'sType': 'RidingAlone' })), 0, 0, 1)
            cl_evact.EventCBRemoveMonsterGroupReward(oTarget, oEventCB, 99, 1)


class CState(cl_state.CState):
    m_SID = 7139
    m_Name = '#NT#轮回9夜姬丸'
    m_DieRemove = 1
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
        2: CallBack2,
        3: CallBack3 }

