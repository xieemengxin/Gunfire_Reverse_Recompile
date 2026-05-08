# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2507.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2507.pyc
# Source Generated with Decompyle++
# File: p2507.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func304, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32372) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 32383) == 0 and cl_evcon.CheckBulletHit(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.0075 + Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.005 * Func410(*a, **{
'sid': 32400 }) / 10000))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32372) == 0 and cl_evcon.CheckHasState(oWarrior, oEventCB, 32383) == 0 and cl_evcon.CheckBulletHit(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.0125 + Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.0075 * Func410(*a, **{
'sid': 32400 }) / 10000))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckBulletHit(oWarrior, oEventCB) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32383) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.015 + Func304(*a, **{
'sAttr': 'EnergyMax' }) * 0.01 * Func410(*a, **{
'sid': 32400 }) / 10000))


class CPerform(CCustomPerform):
    m_SID = 2507
    m_Name = '能量汲取'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 106

