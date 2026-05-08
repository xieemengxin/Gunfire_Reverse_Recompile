# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50596.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50596.pyc
# Source Generated with Decompyle++
# File: p50596.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam', (0, None, ((541,), (lambda a0: a0))))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalReceiveHPDam') >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((304, 'HPMax'), (lambda a0: a0 * 0.1)))):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CountNum', (0, None, ((304, 'HPMax'), (lambda a0: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam') // a0 * 0.1))))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam', (0, None, ((304, 'HPMax'), (361, 50596, 'CountNum'), (lambda a0, a1: -a0 * a1 * 0.1))))
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33210, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33210, 500, { }, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33210, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CountNum'), 0, 0, 500)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33210, 0, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33210, 500, { }, 1, 0)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33210, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CountNum'), 0, 0, 500)


class CPerform(CCustomPerform):
    m_SID = 50596
    m_Name = '50596词条'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

