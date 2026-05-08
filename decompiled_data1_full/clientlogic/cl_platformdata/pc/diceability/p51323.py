# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51323.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51323.pyc
# Source Generated with Decompyle++
# File: p51323.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Damage', 4)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33689, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Damage', 8)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33689, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Damage', 16)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33689, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Damage', 24)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExcessChange', 50)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33689, -1, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33689):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33689, 0, {
            'Damage': 0,
            'ExcessChange': 0 }, 0, 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33689, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33689, 'Damage', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Damage'))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33689, 'ExcessChange', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExcessChange'))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33689, 'Damage', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Damage'))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33689, 'ExcessChange', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExcessChange'))


class CPerform(CCustomPerform):
    m_SID = 51323
    m_Name = '储灵打击'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

