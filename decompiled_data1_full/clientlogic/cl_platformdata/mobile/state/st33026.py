# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33026.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33026.pyc
# Source Generated with Decompyle++
# File: st33026.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1914, 1, 1) and cl_evcon.EventCBGetHitVictimCnt(oTarget, oEventCB):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' }))):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' })), None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 1)
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
    elif cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0):
        cl_evact.EventChangeDamCrazyEff(oTarget, oEventCB, 0, (lambda *a: Func361(*a, **{
'sid': 50004,
'sArgs': 'CrazyEffAddition' })))


def CallBack5(oEventCB, oTarget):
    if not cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        if not cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' }))):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' })), None)
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 1)
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        elif cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0):
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


def CallBack6(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 33026, (lambda *a: Func361(*a, **{
'sid': 50004,
'sArgs': 'MaxNum' })), -1, None)


def CallBack7(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        if not cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' }))):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func361(*a, **{
'sid': 50004,
'sArgs': 'ConsumerNum' })), None)
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 1)
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        elif cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33026ThisFire', 0):
            cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


class CState(cl_state.CState):
    m_SID = 33026
    m_Name = '雷光贯虹'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7 }

