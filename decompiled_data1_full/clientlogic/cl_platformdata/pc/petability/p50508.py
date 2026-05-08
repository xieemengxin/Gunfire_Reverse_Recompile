# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50508.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50508.pyc
# Source Generated with Decompyle++
# File: p50508.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_WEAPON, DAM_USE_HP, OBJ_SELF, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostNum', (0, None, ((208,), (lambda a0: a0))))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') // 10)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostNum', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * 10)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * a0 * 0.05))), 0 | DAM_USE_HP, 0, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostNum', (0, None, ((215,), (lambda a0: a0))))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') // 10)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostNum', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * 10)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * a0 * 0.05))), 0 | DAM_USE_HP, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostNum') // 10)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostNum', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * 10)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * a0 * 0.05))), 0 | DAM_USE_HP, 0, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: a0 * 0.05))), 0 | DAM_USE_HP, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 50508
    m_Name = 'D8'
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
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

