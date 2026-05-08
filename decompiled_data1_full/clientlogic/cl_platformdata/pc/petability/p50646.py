# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50646.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50646.pyc
# Source Generated with Decompyle++
# File: p50646.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import HATEMETHOD_HERODIS, OBJECT_OWNER, PET_ABILITY_LOW, PET_ABILITY_TYPE_ONLYCLONE, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, WARRIOR_PET_MINICLONE

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_PET_MINICLONE):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 1)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, OBJECT_OWNER, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
        'Range': 99 })
    cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 2, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckReason(oWarrior, oEventCB, 'EnterBattle', 0):
        cl_evact.EventCBGetEventMiniClone(oWarrior, oEventCB)
        if cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB):
            cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, OBJECT_OWNER, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
                'Range': 99 })
            cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 2, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckInPointState(oWarrior, oEventCB, {
        33208: 1 }):
        cl_evact.EventCBGetLockEnemy(oWarrior, oEventCB, OBJECT_OWNER, 1, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, HATEMETHOD_HERODIS, {
            'Range': 99 })
        cl_evact.EventCBUseEnableSpell(oWarrior, oEventCB, 2, 0)


class CPerform(CCustomPerform):
    m_SID = 50646
    m_Name = 'M6'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYCLONE
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = {
        'RelifeTime': (0, -5000, 0) }

