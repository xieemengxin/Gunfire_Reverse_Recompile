# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50670.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50670.pyc
# Source Generated with Decompyle++
# File: p50670.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, PET_ABILITY_NORMAL, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p50557_MoveDis', OBJECT_OWNER, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRecordMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'p50557_MoveDis')
    if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((340, 'p50557_MoveDis'), (lambda a0: a0)))) >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnemyNum', (0, None, ((340, 'p50557_MoveDis'), (lambda a0: a0 // 10))))
        cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'p50557_MoveDis', -10 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 25, WARRIOR_MONSTER, 1, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'), 0, 1, 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 25, WARRIOR_MONSTER, 1, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnemyNum'), 0, 1, 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, 1, {
        'CardNum': 3,
        'QualityNum': 1,
        'AssignEndPos': {
            206: 1,
            207: 1,
            213: 1,
            217: 1 },
        'CustomData': {
            217: {
                'DamMul': 1,
                'pf7009_throw': 1 } } })


class CPerform(CCustomPerform):
    m_SID = 50670
    m_Name = '50670'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

