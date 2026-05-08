# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13101.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13101.pyc
# Source Generated with Decompyle++
# File: p13101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 9094, 'InsEnhance', 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1906, 0, { }, 1)
    if cl_condition.PassiveCheckFromMainHoldWeapon(oWarrior, oLifeCycle):
        cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 13101, '13101Deputy', 0)
    else:
        cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 13101, '13101Deputy', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oWarrior, oLifeCycle, 9094, 'InsEnhance', 0)
    if not oLifeCycle.m_Owner.GetArgValue('13101Deputy'):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1905, 0, 1, 0, 0):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 100)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCbGetTargetByStateTargetData(oWarrior, oEventCB, 1906)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, 1905)


class CPerform(CCustomPerform):
    m_SID = 13101
    m_Name = '六方专属一'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1007,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

