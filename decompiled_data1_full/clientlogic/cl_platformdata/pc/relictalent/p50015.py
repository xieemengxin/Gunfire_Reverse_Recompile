# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50015.pyc
# Source Generated with Decompyle++
# File: p50015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oLifeCycle, 50021, -1600, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oLifeCycle, 50021, -2600, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oLifeCycle, 50021, -3600, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214) == 0 and cl_condition.CheckHero(oWarrior, oLifeCycle, 213) == 0:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 600, {
            'StatusEffect': -1600,
            'KeepTime': 600 }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 800, {
            'StatusEffect': -2600,
            'KeepTime': 800 }, 1, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 1000, {
            'StatusEffect': -3600,
            'KeepTime': 1000 }, 1, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32774):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 600, {
            'StatusEffect': -1600,
            'KeepTime': 600 }, 1, 1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32774):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 800, {
            'StatusEffect': -2600,
            'KeepTime': 800 }, 1, 1, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 32774):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33012, 1000, {
            'StatusEffect': -3600,
            'KeepTime': 1000 }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 50015
    m_Name = '生生不息'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
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

