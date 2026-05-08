# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50600.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50600.pyc
# Source Generated with Decompyle++
# File: p50600.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, DAM_USE_HP, DPSUBMSG_DEFAULT, OBJ_ATTACK, OBJ_SELF, PET_ABILITY_NORMAL
from cl_item.defines import EQUIP_LASER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT, 0)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((548,), (lambda a0: a0)))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, (0, None, ((548,), (304, 'HPMax'), (lambda a0, a1: (a0 * a1 * 1 / 100) * -1))), DAM_USE_HP, 0)
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'p50600_Buff', 1)
    elif cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'p50600_Buff', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'p50600_Buff', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'p50600_Buff'):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (0, None, ((548,), (lambda a0: 100 * a0))), 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (0, None, ((548,), (lambda a0: a0))))


class CPerform(CCustomPerform):
    m_SID = 50600
    m_Name = '50600词条'
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

