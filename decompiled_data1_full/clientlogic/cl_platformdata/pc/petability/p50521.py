# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50521.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50521.pyc
# Source Generated with Decompyle++
# File: p50521.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_SELF, PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYCLONE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 50521, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not oWarrior.HP() > 100 or cl_evcon.CheckTargetPetPointBaseMonster(oWarrior, oEventCB, 2221) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            7304: 1 }, 1, 0):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33190, 800, { }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetPetPointBaseMonster(oWarrior, oEventCB, 2221):
        cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, 20000, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50521
    m_Name = 'Q1'
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
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

