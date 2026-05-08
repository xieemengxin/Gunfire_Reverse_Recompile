# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16069.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16069.pyc
# Source Generated with Decompyle++
# File: p16069.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func340

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'pf16069', None, None)
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32682):
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 50 * Func340(*a, **{
'sKey': 'pf16069' })), 0)
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf16069', None, None, None)


class CPerform(CCustomPerform):
    m_SID = 16069
    m_Name = '烈火足迹'
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

