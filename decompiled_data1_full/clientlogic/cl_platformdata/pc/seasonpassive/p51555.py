# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51555.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51555.pyc
# Source Generated with Decompyle++
# File: p51555.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39728):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39728, 0, { }, 0)
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, 1, 'PF-51555')
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, -1, 'PF-51555')
    if not cl_condition.GetStateStatistics(oWarrior, oLifeCycle, 39728, 'PF-51555'):
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 39728, 0)


def Action2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39728):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39728, 0, { }, 0)
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, 1, 'PF-51555')
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, -1, 'PF-51555')
    if not cl_condition.GetStateStatistics(oWarrior, oLifeCycle, 39728, 'PF-51555'):
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 39728, 0)


def Action3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39728):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39728, 0, { }, 0)
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, 1, 'PF-51555')
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 39728, -1, 'PF-51555')
    if not cl_condition.GetStateStatistics(oWarrior, oLifeCycle, 39728, 'PF-51555'):
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 39728, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39728, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51555
    m_Name = '#NT#暴击'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

