# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6108.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6108.pyc
# Source Generated with Decompyle++
# File: p6108.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_CURE, OBJ_SELF, WARRIOR_ELITE, WARRIOR_MONSTER, WARRIOR_NORBOX

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7934, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 3)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7934, 1, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1000, 1000, 5)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7934, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7953, 150, { }, 1, 0, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, None, None, {
        24011: 10 }, None, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) >= 1:
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7948, 150, { }, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7953, 150, { }, 1, 0, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, None, None, {
        24011: 10 }, None, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) >= 1:
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7949, 150, { }, 1, None, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7953, 150, { }, 1, 0, None)
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, None, None, {
        24011: 10 }, None, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) >= 1:
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 6)


def DoCallBackAction6(oEventCB, oWarrior):
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7950, 150, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 6108
    m_Name = '治愈的'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_CURE

