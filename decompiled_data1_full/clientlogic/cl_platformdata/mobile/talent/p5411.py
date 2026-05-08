# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5411.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5411.pyc
# Source Generated with Decompyle++
# File: p5411.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK
from cl_newformula import Func303, Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11083, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11083, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11083, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponBulletCnt(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'MaxBullet' }) * 100 / 100 + 0)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: Func308(*a) * 3000 + 0), 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 10 + Func308(*a) * 10))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckBulletFull(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32213, 0, { }, 1, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponBulletCnt(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'MaxBullet' }) * 100 / 100 + 0)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 10000, 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 10 + Func308(*a) * 10))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckBulletFull(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32214, 0, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5411
    m_Name = '子弹风暴'
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
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 103

