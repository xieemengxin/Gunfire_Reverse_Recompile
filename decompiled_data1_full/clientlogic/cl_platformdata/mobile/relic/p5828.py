# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5828.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5828.pyc
# Source Generated with Decompyle++
# File: p5828.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_NORMAL, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func438

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1444, 1, 1, None) == 0:
        if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            12013: 1,
            1315: 1,
            1319: 1,
            8505: 1 }, 1, 1):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1444, 10, { }, 1, 0, None)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func438(*a) * 50 / 100), DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, None, None, None, None, None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1444, 1, 1, None) == 0:
        if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            12009: 1,
            1315: 1,
            1319: 1,
            8505: 1 }, 1, 1):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1444, 10, { }, 1, 0, None)
            cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 50, 1, 0, 0, 1, None, None, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) == 1 or cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1444, 1, 1, None) == 0:
            if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
                12009: 1,
                1315: 1,
                1319: 1,
                8505: 1 }, 1, 1):
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1444, 10, { }, 1, 0, None)
                cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 50, 1, 0, 0, 1, None, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5828
    m_Name = '元素弹夹'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

