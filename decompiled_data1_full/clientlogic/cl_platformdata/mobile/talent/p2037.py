# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2037.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2037.pyc
# Source Generated with Decompyle++
# File: p2037.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_AMULET, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Radius', 0, 2)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 20, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 20, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Radius', 2, 0, { }, {
        2: 1,
        22: 1 })


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Radius', 0, 4)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 21, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 21, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 1, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Radius', 4, 0, { }, {
        2: 1,
        22: 1 })


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Radius', 0, 6)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 22, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL, 22, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 2, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Radius', 6, 0, { }, {
        2: 1,
        22: 1 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 2) or cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 22):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'Radius', 2, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 2) or cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 22):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'Radius', 4, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 2) or cl_evcon.CheckEventWeaponClassifyTag(oWarrior, oEventCB, 22):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'Radius', 6, 0)


def DoCallBackAction20(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 3000, 0, 0, '')


def DoCallBackAction21(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 4500, 0, 0, '')


def DoCallBackAction22(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_TYPE_AMULET) == 0:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 10000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 2037
    m_Name = '强化爆炸'
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
        20: DoCallBackAction20,
        21: DoCallBackAction21,
        22: DoCallBackAction22 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 101

