# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5021.pyc
# Source Generated with Decompyle++
# File: p5021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import EXTGRADE_GROUP2, INSCRIPTION_TYPE_EXCLUSIVE, INSCRIPTION_TYPE_RARE, MAIN_HOLD
from cl_newformula import Func526

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GREATEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DROPWEAPON, -1, 5, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBTempOpenWeaponExclusiveIns(oWarrior, oEventCB, 2)
    cl_evact.EventCBChangeItemGradeBySource(oWarrior, oEventCB, 5, {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeWeaponInscriptionNumBySource(oWarrior, oEventCB, INSCRIPTION_TYPE_EXCLUSIVE, 2, {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1 }, INSCRIPTION_TYPE_RARE)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)
        cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func526(*a) * 3 // 10), MAIN_HOLD, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)
    cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func526(*a) * 3 // 10), MAIN_HOLD, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBRemoveTempOpenWeaponExclusiveIns(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 5021
    m_Name = '泼天气运'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 111

