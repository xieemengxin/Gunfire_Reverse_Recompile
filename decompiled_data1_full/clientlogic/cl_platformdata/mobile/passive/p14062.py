# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14062.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14062.pyc
# Source Generated with Decompyle++
# File: p14062.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33814, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CastingSkill', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33813):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CastingSkill', 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CastingSkill', 1)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33813, 1500, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 5)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33813):
        cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33813, 500, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33813 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CastingSkill'):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33813, 1500, { }, 1)
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 5)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 22062, 1, 0):
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33813):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CastingSkill', 1)
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CastingSkill', 1)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33813, 1500, { }, 1)
            cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 100, 100, 5)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 22062, 1, 0):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 33813):
            cl_evact.EventCBSetStateTime(oWarrior, oEventCB, 33813, 500, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CastingSkill', 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33813, 5, 0)


class CPerform(CCustomPerform):
    m_SID = 14062
    m_Name = '轮回9-激光龟激光提供护盾'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
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

