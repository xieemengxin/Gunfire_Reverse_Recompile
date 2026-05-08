# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/survivormonsteraf/p6155.pyc
# RelativePath: clientlogic/cl_perform/survivormonsteraf/p6155.pyc
# Source Generated with Decompyle++
# File: p6155.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.survivormonsteraf import CPerform as CCustomPerform
from cl_commondefines import MAF_TYPE_CLEANSE, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7931, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7044, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7931, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7044, 1, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7931, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7044, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_MONSTER, 0, 1, 0, None, None, {
        24011: 10 }, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetCanAddHaloState(oWarrior, oEventCB, 7931):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7931, 104, { }, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 6155
    m_Name = '坚韧的'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_MonsterAfType = MAF_TYPE_CLEANSE

