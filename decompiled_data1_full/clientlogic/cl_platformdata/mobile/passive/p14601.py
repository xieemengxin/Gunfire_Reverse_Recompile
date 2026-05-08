# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14601.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14601.pyc
# Source Generated with Decompyle++
# File: p14601.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_HERO
from cl_newformula import Func350

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 25, 0)
    cl_action.CommonSetSummonLifeTime(oWarrior, oLifeCycle, 500)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func350(*a)), WARRIOR_HERO, 1, 1, 1, 0, 0, { }, 0, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) >= 0:
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1956, 0, { }, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7968, 25, { }, 0, 0, None)
    cl_action.CommonSelfDie(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 14601
    m_Name = '首领秘卷龙卷风'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1

