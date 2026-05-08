# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5309.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5309.pyc
# Source Generated with Decompyle++
# File: p5309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DUAL_STATE_BEGIN, DUAL_STATE_END

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WIELDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.CommonShareMainPerformPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9094)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IntervalCostTimes', 2)
        cl_action.CommonChangeSourceWeaponPFBulletPerfomrAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse', 0, 10000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckDualWeapon(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.CommonDisableShareMainPerformPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9094)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IntervalCostTimes', 1)
        cl_action.CommonChangeSourceWeaponPFBulletPerfomrAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5309
    m_Name = '六方-双持'
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
    m_BaseArgData = {
        'IntervalCostTimes': 1 }
    m_DieDisable = 1

