# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2039.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2039.pyc
# Source Generated with Decompyle++
# File: p2039.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_AMULET, OBJ_ATTACK
from cl_newformula import Func339

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func339(*a) * 500 + 2000), 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func339(*a) * 700 + 4000), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func339(*a) * 900 + 6000), 0, 0, '')
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: (lambda *a: Func339(*a) * 900) }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func339(*a) * 900 + 6000), 10000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 2039
    m_Name = '爆炸狂魔'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 101

