# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5405.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5405.pyc
# Source Generated with Decompyle++
# File: p5405.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'FillTime', 0, -2000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 1, 0, 0)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'FillTime', 0, -3500, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 2, 0, 0)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'FillTime', 0, -5000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32048, 400, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32048, 500, { }, 1, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32048, 600, { }, 1, 1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, -2000, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, -3500, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, -5000, 0)


class CPerform(CCustomPerform):
    m_SID = 5405
    m_Name = '超频弹夹'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 101

