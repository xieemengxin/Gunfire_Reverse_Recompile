# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4335.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4335.pyc
# Source Generated with Decompyle++
# File: p4335.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1839, 0, { }, 1)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11122, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WIELDWEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveChangeSourceWeaponPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 9396, 'MaxPFBullet', 0, 10000)
        cl_action.PassiveDisableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11122)
        cl_action.PassiveEnableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11125, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveChangeSourceWeaponPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 9396, 'MaxPFBullet', 0, 0)
        cl_action.PassiveDisableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11125)
        cl_action.PassiveEnableBulletChangeRule(oWarrior, oEventCB.GetCBLifeCycle(), 11122, 1)


class CPerform(CCustomPerform):
    m_SID = 4335
    m_Name = '八爪鱼-水枪能量变更'
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

