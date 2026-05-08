# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50642.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50642.pyc
# Source Generated with Decompyle++
# File: p50642.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_HIGH, PET_ABILITY_TYPE_ONLYMAIN, WARRIOR_PET_MINI
from cl_newformula import Func388, Func597, Func701

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func701(*a) * 2000), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeOwnerBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func597(*a) * 100), 0)
    cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBChangeTargetBaseDamRatio(oWarrior, oEventCB, (lambda *a: Func388(*a, **{
'sAttr': 'MoveSpeed' }) * 100), 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_PET_MINI):
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 0)
        cl_action.CommonListenOwnerMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MINICLONE_DIE, -1, 0)
        cl_action.CommonListenOwnerMsgCallBackByAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 1)
    else:
        cl_action.CommonListenOwnerMsgCallBackByAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 6)
        cl_action.CommonChangeOwnerAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 2000, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func388(*a, **{
'sAttr': 'MoveSpeed' }) * 100), 0, 0, 1)
    cl_action.CommonChangeOwnerBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, (lambda *a: Func597(*a) * 100), 0)


class CPerform(CCustomPerform):
    m_SID = 50642
    m_Name = 'M2'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_NeedLockTarget = 0
    m_EnableType = PET_ABILITY_TYPE_ONLYMAIN
    m_Quality = PET_ABILITY_HIGH
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

