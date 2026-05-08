# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5009.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5009.pyc
# Source Generated with Decompyle++
# File: p5009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func340

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1596, 0, { }, -1)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'pf5009', None, None)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1596):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1596, (lambda *a: 1 * Func340(*a, **{
'sKey': 'pf5009' })), None)
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf5009', None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5009
    m_Name = '蓄势待发'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 1
    m_Career = 103

