# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50514.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50514.pyc
# Source Generated with Decompyle++
# File: p50514.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_SELF, PET_ABILITY_NORMAL, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 8, WARRIOR_MONSTER, 0, 0, 10, 0, 0, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RangeCount', cl_evact.EventGetTargetNum(oWarrior, oEventCB))
    cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 8, WARRIOR_MONSTER, 0, 0, 10, 0, 0, 0)
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RangeCount', cl_evact.EventGetTargetNum(oWarrior, oEventCB))
    cl_action.CommonChangeOwnerBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 3000 * min(10, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RangeCount')))


class CPerform(CCustomPerform):
    m_SID = 50514
    m_Name = 'Z4'
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
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

