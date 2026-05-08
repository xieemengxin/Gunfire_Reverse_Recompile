# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6156.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6156.pyc
# Source Generated with Decompyle++
# File: p6156.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, CURE_TYPE_SCENE, MAF_TYPE_UNYIELD, WARRIOR_ELITE, WARRIOR_MONSTER, WARRIOR_NORBOX

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7932, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7045, 1, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7932, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7045, 1, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7932, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7045, 1, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 3, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_MONSTER, 0, 1, 0, None, None, {
        24011: 10 }, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBOX):
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 5)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCallBackChangeCure(oWarrior, oEventCB, CURE_TYPE_PERFORM | CURE_TYPE_SCENE, -8000, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetCanAddHaloState(oWarrior, oEventCB, 7932):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7932, 104, { }, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 6156
    m_Name = '坚固的'
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
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_UNYIELD

