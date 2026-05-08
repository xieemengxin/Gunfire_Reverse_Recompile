# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40066.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40066.pyc
# Source Generated with Decompyle++
# File: p40066.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import EXTGRADE_GROUP2, MAIN_HOLD, TASK_CHOOSEFUN_END

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.PassiveClearTaskTempDisableInsciption(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetTaskSaveInfo(oWarrior, oEventCB, 'ChooseUpgradeInscription'):
        cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, -1, MAIN_HOLD, None)
        cl_evact.PassiveCBTaskTempDisableInscription(oWarrior, oEventCB, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECAST_INSCRIPTION, -1, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, -1, 6, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TASK, TASK_CHOOSEFUN_END, 7, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBRefreshTaskDisableInscription(oWarrior, oEventCB, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBReplaceTaskDisableInscription(oWarrior, oEventCB)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBChangeWeaponExtGrade(oWarrior, oEventCB, EXTGRADE_GROUP2, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBTaskTempDisableInscription(oWarrior, oEventCB, 1)
    cl_evact.EventCBChangeWeaponExtGrade(oWarrior, oEventCB, EXTGRADE_GROUP2, -1)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBTaskTempDisableInscription(oWarrior, oEventCB, 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetTaskSaveInfo(oWarrior, oEventCB, 'ChooseUpgradeInscription'):
        cl_action.CommonChangeWeaponExtGrade(oWarrior, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, -1, MAIN_HOLD, None)
        cl_evact.PassiveCBTaskTempDisableInscription(oWarrior, oEventCB, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_RECAST_INSCRIPTION, -1, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, -1, 6, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 40066
    m_Name = '天降大任-武器锻造1特殊效果'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

