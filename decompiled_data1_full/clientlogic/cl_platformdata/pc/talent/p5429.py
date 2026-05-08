# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5429.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5429.pyc
# Source Generated with Decompyle++
# File: p5429.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, EQUIP_HANDGUN, EQUIP_TYPE_FUNDAMENTALWEAPON, MAIN_HOLD, OBJ_ATTACK
from cl_newformula import Func308, Func362

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32896, 0, { }, -1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32896, 0, { }, -1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32896, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 100 * Func308(*a) * Func362(*a, **{
'sAttr': 'MoveSpeed' })), 0, DAM_TYPE_WEAPON, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_HANDGUN) or cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 2000, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_HANDGUN) or cl_condition.CheckWeaponTypeByHoldType(oWarrior, oEventCB.GetCBLifeCycle(), MAIN_HOLD, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 4000, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5429
    m_Name = '战斗步伐'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 114

