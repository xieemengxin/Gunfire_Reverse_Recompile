# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15167.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15167.pyc
# Source Generated with Decompyle++
# File: p15167.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33374, 0, {
        'TalentLevel': 1 }, 1)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 500, 0)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'CountMax', 5, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15167)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33374, 0, {
        'TalentLevel': 2 }, 1)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 400, 0)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'CountMax', 5, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15167)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33374, 0, {
        'TalentLevel': 3 }, 1)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 300, 0)
    cl_action.CommonSetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'CountMax', 10, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), cl_action.CommonGetSeasonSuitArg(oWarrior, oLifeCycle, 15101, 'AddCountTime', 0), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15167)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 33374 }))) < cl_action.CommonGetSeasonSuitArg(oWarrior, oEventCB.GetCBLifeCycle(), 15101, 'CountMax', 0):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33374, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33374, 0)
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), cl_action.CommonGetSeasonSuitArg(oWarrior, oEventCB.GetCBLifeCycle(), 15101, 'AddCountTime', 0), cl_action.CommonGetSeasonSuitArg(oWarrior, oEventCB.GetCBLifeCycle(), 15101, 'AddCountTime', 0), 0)


class CPerform(CCustomPerform):
    m_SID = 15167
    m_Name = '暴击之眼'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

