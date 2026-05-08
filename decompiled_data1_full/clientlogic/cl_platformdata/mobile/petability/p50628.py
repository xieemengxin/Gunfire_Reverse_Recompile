# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/petability/p50628.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/petability/p50628.pyc
# Source Generated with Decompyle++
# File: p50628.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, PET_ABILITY_NORMAL, PET_ABILITY_TYPE_ONLYCLONE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) == 100:
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33298):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33298, 800, { }, 1)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33298, 1, 800)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 // 1000), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 50628
    m_Name = 'D4'
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
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_NORMAL
    m_LimitPet = ()
    m_ExcludePet = (2001, 2002, 2421)
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }
    m_AIMemberPetDisable = True

