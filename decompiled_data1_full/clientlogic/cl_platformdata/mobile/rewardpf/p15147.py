# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15147.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15147.pyc
# Source Generated with Decompyle++
# File: p15147.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func236, Func377

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func236(*a))) == 0 or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func377(*a))) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33459, 0, { }, 1)
    else:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33459)


class CPerform(CCustomPerform):
    m_SID = 15147
    m_Name = '幽影无暇'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

