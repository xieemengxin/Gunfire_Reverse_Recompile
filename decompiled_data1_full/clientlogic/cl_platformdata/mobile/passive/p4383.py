# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4383.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4383.pyc
# Source Generated with Decompyle++
# File: p4383.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CAREERPF, PF_TYPE_THROW, WARRIOR_MONSTER, WARRIOR_PROTEGE_NORMAL
from cl_newformula import Func685, Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPFRecoverWeaponPFBullet(oWarrior, oLifeCycle, {
        9701: 200,
        9792: 200,
        1918: 25,
        1921: 25 }, 50)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if (cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9701: 1,
        9792: 1 }, 0, 0)) and cl_evcon.CheckAttackInShield(oWarrior, oEventCB) == 0:
        if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_PROTEGE_NORMAL):
            cl_evact.EventCBAddSourceWeaponPFBullet(oWarrior, oEventCB, 9791, (lambda *a: Func686(*a, **{
'iPerform': 9791,
'sAttr': 'PFBulletRecover' }) * Func685(*a) // 100), 1, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if (cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0) or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0)) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBAddSourceWeaponPFBullet(oWarrior, oEventCB, 9791, (lambda *a: Func686(*a, **{
'iPerform': 9791,
'sAttr': 'PFBulletRecover' }) * Func685(*a) // 100), 1, 1)


class CPerform(CCustomPerform):
    m_SID = 4383
    m_Name = '标记法杖充能被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

