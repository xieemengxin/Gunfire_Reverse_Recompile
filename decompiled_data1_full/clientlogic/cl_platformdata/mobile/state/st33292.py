# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33292.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33292.pyc
# Source Generated with Decompyle++
# File: st33292.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336, Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217) == 0 and cl_condition.CheckHero(oTarget, oLifeCycle, 219) == 0:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 217):
        cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 2)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 4, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 1)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 2000), DAM_TYPE_WEAPON, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 2000), 0, DAM_TYPE_WEAPON, '')


def CallBack1(oEventCB, oTarget):
    if (cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, 0)) and cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 1)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 2000), DAM_TYPE_WEAPON, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 2000), 0, DAM_TYPE_WEAPON, '')


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 0) <= 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1305, 1, -1) == 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1323, 1, -1) == 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1310, 1, -1) == 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0 and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 0) <= 0 and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1325, 1, -1) == 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1322, 1, -1):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'CartoonFlag' }))) == 1 and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 0) <= 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 33292
    m_Name = '#NT#法杖铭刻武器伤害加成'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

