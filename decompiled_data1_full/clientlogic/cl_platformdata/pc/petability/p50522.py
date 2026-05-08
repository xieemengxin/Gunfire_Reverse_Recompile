# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50522.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50522.pyc
# Source Generated with Decompyle++
# File: p50522.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJECT_OWNER, PET_ABILITY_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p50522_MoveDis', OBJECT_OWNER, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRecordMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'p50522_MoveDis')
    if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((340, 'p50522_MoveDis'), (lambda a0: a0)))) >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnemyNum', (0, None, ((340, 'p50522_MoveDis'), (lambda a0: a0 // 10))))
        cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'p50522_MoveDis', -10 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'))
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33261, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'), 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33261, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'), 0, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33261, 0, { }, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50522
    m_Name = 'Q2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

