# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5710.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5710.pyc
# Source Generated with Decompyle++
# File: p5710.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func303, Func505, Func511

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponBulletCnt(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'MaxBullet' }) * 100 / 100 + 0)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckBulletFull(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1078, 0, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func511(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 70 / 100 + 0)):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 6000, 0, 0, '')


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckBulletRatio(oWarrior, oEventCB, 70):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1088, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5710
    m_Name = '先声夺人'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

