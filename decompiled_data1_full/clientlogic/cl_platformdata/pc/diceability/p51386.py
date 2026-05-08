# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51386.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51386.pyc
# Source Generated with Decompyle++
# File: p51386.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_AI, DICETAG_SEASONOUTPUT, OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1750)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 1500)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1750)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 2000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1750)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 3000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1750)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 4000)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 30, WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1750, {
            'Cnt': (lambda *a: Func717(*a, **{
'sArg': 'Cnt' })),
            'AIDamFactor': (lambda *a: Func717(*a, **{
'sArg': 'AIDamFactor' })) }, 0)


class CPerform(CCustomPerform):
    m_SID = 51386
    m_Name = '鸿运流星'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT, DICETAG_AI)

