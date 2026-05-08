# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50586.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50586.pyc
# Source Generated with Decompyle++
# File: p50586.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, OBJ_ENEMY, PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetRangeTargetByTargetType(oWarrior, oEventCB, 7, OBJ_ENEMY, 0)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: a0))), DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, 0, 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 50586, 0)


class CPerform(CCustomPerform):
    m_SID = 50586
    m_Name = ''
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
    m_DieDisable = 0
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

