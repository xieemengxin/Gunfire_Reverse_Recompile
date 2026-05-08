# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25807.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25807.pyc
# Source Generated with Decompyle++
# File: p25807.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_FRIEND_NOSELF, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1683, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1822, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 15, OBJ_FRIEND_NOSELF, 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1683, 100, { }, 1, 0, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1822, 100, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 25807
    m_Name = '极速支援'
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
    m_RelicType = 0
    m_HeroRelic = 5807
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

