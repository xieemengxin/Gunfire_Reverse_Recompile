# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14600.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14600.pyc
# Source Generated with Decompyle++
# File: p14600.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetDieRemoveDelay(oWarrior, oLifeCycle, 310)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 300, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7987, 0, { }, -1)
    cl_action.CommonSetSkillCheckArgs(oWarrior, oLifeCycle, 1, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 60, WARRIOR_HERO, 1, 0, 1, 0, 0, { }, -1, None, None, None, None)
    cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
        39218: 0 })


class CPerform(CCustomPerform):
    m_SID = 14600
    m_Name = '首领秘卷小触手'
    m_MaxLevel = 1
    m_MaxStack = 0
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1

