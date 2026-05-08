# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15040.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15040.pyc
# Source Generated with Decompyle++
# File: p15040.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import EXTGRADE_GROUP2, MAIN_HOLD
from cl_newformula import Func526

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDoneEvent(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
        cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)
        cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func526(*a) * 15 // 100), MAIN_HOLD, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBClearExtGrade(oWarrior, oEventCB)
    cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func526(*a) * 15 // 100), MAIN_HOLD, 0)


class CPerform(CCustomPerform):
    m_SID = 15040
    m_Name = '如意神兵'
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

