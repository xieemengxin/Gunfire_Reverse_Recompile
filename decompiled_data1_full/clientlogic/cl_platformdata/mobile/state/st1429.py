# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1429.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1429.pyc
# Source Generated with Decompyle++
# File: st1429.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_UPGRADEWEAPON, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func207

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-0', 1)
    if cl_evcon.CheckTriggerLuckyHit(oTarget, oEventCB):
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-1', 1)
    elif cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None):
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: max(-2, int(Func207(*a) * -100 / 100 + 0))), 0, JUMPFIGURE_UPGRADEWEAPON, 0, None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-0', None) > 0 and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-1', None) == 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= 2:
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: max(-2, int(Func207(*a) * -100 / 100 + 0))), 0, JUMPFIGURE_UPGRADEWEAPON, 0, None)


def CallBack4(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= 2:
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-0', 1)
        if cl_evcon.CheckTriggerLuckyHit(oTarget, oEventCB):
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'PF5756-1-1', 1)
        elif cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None):
            cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: max(-2, int(Func207(*a) * -100 / 100 + 0))), 0, JUMPFIGURE_UPGRADEWEAPON, 0, None)


def CallBack5(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= 2:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 30)


class CState(cl_state.CState):
    m_SID = 1429
    m_Name = '#NT#新投币攻击'
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
        0: CallBack0,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5 }

