# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51263.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51263.pyc
# Source Generated with Decompyle++
# File: p51263.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_TYPE_POSITIVE, LEVEL_TYPE_HIDE, WANDCOMP_TRIGGER_ACTION
from cl_newformula import Func361, Func779

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMP, WANDCOMP_TRIGGER_ACTION, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerMaxCount', (lambda *a: Func779(*a) * 3))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurTriggerCount') > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TriggerMaxCount'):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WANDCOMP, WANDCOMP_TRIGGER_ACTION)
    else:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurTriggerCount', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurAddition', (lambda *a: Func361(*a, **{
'sid': 51263,
'sArgs': 'CurTriggerCount' }) // Func779(*a)))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurAddition') > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AlreadyAdditionCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AlreadyAdditionCount', (lambda *a: Func361(*a, **{
'sid': 51263,
'sArgs': 'CurAddition' })))
            cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', 0, (lambda *a: -Func361(*a, **{
'sid': 51263,
'sArgs': 'AlreadyAdditionCount' }) * 1000), 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AlreadyAdditionCount', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurTriggerCount', 0)
        cl_evact.PassiveCBChangeWandAttr(oWarrior, oEventCB, 'ColdTime', 0, 0, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_WANDCOMP, WANDCOMP_TRIGGER_ACTION, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51263
    m_Name = '过载能力2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = {
        'AlreadyAdditionCount': 0 }
    m_DieDisable = 0
    m_QualityValue = { }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 10
    m_IsReverseFloting = 1

