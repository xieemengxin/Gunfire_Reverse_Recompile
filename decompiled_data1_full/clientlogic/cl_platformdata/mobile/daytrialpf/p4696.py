# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4696.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4696.pyc
# Source Generated with Decompyle++
# File: p4696.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_BOSS, WARRIOR_ELIMAGIC, WARRIOR_ELISMANEAR, WARRIOR_NORBADGER, WARRIOR_NORLARGESUMMON, WARRIOR_NORMAGIC

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 600, 600, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_ELIMAGIC)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_NORLARGESUMMON)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_NORMAGIC)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_ELISMANEAR)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_NORBADGER)
    cl_evact.EventExcludeTargetByFightType(oWarrior, oEventCB, WARRIOR_BOSS)
    cl_evact.EventExcludeTargetByState(oWarrior, oEventCB, 7951)
    cl_evact.EventExcludeTargetByState(oWarrior, oEventCB, 1360)
    cl_evact.EventRandomTargetExecCBFuncAction(oWarrior, oEventCB, 1, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1360, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4696
    m_Name = '庇护灵石'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

