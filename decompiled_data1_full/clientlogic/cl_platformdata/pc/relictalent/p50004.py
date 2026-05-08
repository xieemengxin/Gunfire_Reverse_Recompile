# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50004.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50004.pyc
# Source Generated with Decompyle++
# File: p50004.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import DPSUBMSG_DEFAULT, DUAL_STATE_END, OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func308, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', -20, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDERPLUS, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 207) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 217) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 219) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, -1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', 20, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', -30, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDERPLUS, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 207) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 217) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 219) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, -1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', 30, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', -40, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDERPLUS, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 207) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 217) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 219) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, -1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 50007, 'MoveDistance', 40, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsThunderPlus', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsThunderPlus'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsThunderPlus', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func308(*a) * 20 + 30))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsThunderPlus'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsThunderPlus', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func308(*a) * 20 + 30))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1321: 1,
        1322: 1 }, 1, 0) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsThunderPlus'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsThunderPlus', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func308(*a) * 20 + 30))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 33017, (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'MoveDistance' })), -1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33044) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsThunderPlus'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsThunderPlus', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBSubTargetCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func308(*a) * 20 + 30))


class CPerform(CCustomPerform):
    m_SID = 50004
    m_Name = '雷光贯虹'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

