# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51317.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51317.pyc
# Source Generated with Decompyle++
# File: p51317.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_ONE

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'GainEffect', 3000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'GainEffect', 4000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 1000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'GainEffect', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'GainEffect', 10000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 4000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33679):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33679, 0, {
            'AbnormalSourceDam': 0,
            'GainEffect': 0 }, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33679, 'GainEffect', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'GainEffect'))
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33679, -1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33679, 'GainEffect', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'GainEffect'))
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33679, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33679, 'AbnormalSourceDam', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AbnormalSourceDam'))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 33679, 'AbnormalSourceDam', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AbnormalSourceDam'))


class CPerform(CCustomPerform):
    m_SID = 51317
    m_Name = '元素专精'
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
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

