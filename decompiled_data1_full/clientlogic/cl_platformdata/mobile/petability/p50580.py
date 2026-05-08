# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50580.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50580.pyc
# Source Generated with Decompyle++
# File: p50580.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_USE_HP, OBJ_SELF, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > 5:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: -a0 * 5 / 100))), DAM_USE_HP, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam', (0, None, ((541,), (lambda a0: a0))))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TotalReceiveHPDam') >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((304, 'HPMax'), (lambda a0: a0 * 0.3)))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CountNum', (0, None, ((304, 'HPMax'), (lambda a0: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam') // a0 * 0.3))))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam', (0, None, ((3, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TotalReceiveHPDam'), ((304, 'HPMax'), (lambda a0: a0 * 0.3))), (lambda a0: a0))))
        cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CountNum'), None)


class CPerform(CCustomPerform):
    m_SID = 50580
    m_Name = ''
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
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

