# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50597.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50597.pyc
# Source Generated with Decompyle++
# File: p50597.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, PET_ABILITY_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > 1:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, (0, None, ((304, 'HPMax'), (lambda a0: -a0 * 1 / 100))), DAM_USE_HP, 0)
        cl_evact.EventCBAddDamSign(oWarrior, oEventCB, 'pf_50597', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamSign(oWarrior, oEventCB, 'pf_50597'):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 50597
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

