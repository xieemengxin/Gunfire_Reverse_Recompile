# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50604.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50604.pyc
# Source Generated with Decompyle++
# File: p50604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import OBJ_VICTIM, PET_ABILITY_NORMAL, SCENE_EVT_SHAPE_SPHERE
from cl_pxlayer import PXLAYER_TRIGGERDYNA

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddEvent(oWarrior, oEventCB, 0, SCENE_EVT_SHAPE_SPHERE, {
        'Radius': 5 }, 1, 2, 1, PXLAYER_TRIGGERDYNA)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33205, 0, { }, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsSelfOwner(oWarrior, oEventCB):
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33205, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 50604
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
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

