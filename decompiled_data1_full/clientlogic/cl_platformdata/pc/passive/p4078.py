# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4078.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4078.pyc
# Source Generated with Decompyle++
# File: p4078.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import STATE_CLS_ABNORMAL, STATUS_PUSH, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 10, 0)
    cl_action.CommonRemoveAllStateByType(oWarrior, oLifeCycle, STATE_CLS_ABNORMAL)
    cl_action.CommonSetSkillCheckArgs(oWarrior, oLifeCycle, 20, 6)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7938, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 7, WARRIOR_HERO, 1, 1, None, None, None, { }, None, None, None, None, None)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTargetMoveStatus(oWarrior, oEventCB, STATUS_PUSH) == 0:
        cl_evact.EventCBPushHeroTarget(oWarrior, oEventCB, 20, 5, 5, 9.8, 45)
        cl_evact.EventClientBehavior(oWarrior, oEventCB, 7953, 0)


class CPerform(CCustomPerform):
    m_SID = 4078
    m_Name = '二幕Boss阶段3潜行'
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
    m_DieDisable = 1

