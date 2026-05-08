# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50632.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50632.pyc
# Source Generated with Decompyle++
# File: p50632.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func304, Func683

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostRatio', (lambda *a: Func683(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostRatio') >= 10:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostRatio') // 10)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostRatio', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * 10)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') * Func304(*a, **{
'sAttr': 'HPMax' }) * 5 / 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50632
    m_Name = 'D8'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = {
        'HPMax': (0, 7500, 0) }
    m_AIMemberPetDisable = True

