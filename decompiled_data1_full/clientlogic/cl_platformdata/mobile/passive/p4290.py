# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4290.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4290.pyc
# Source Generated with Decompyle++
# File: p4290.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_VICTIM, WARRIOR_BOSS
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1523) == 0 and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9007: 1 }, 1, 0) and cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventCBAddSourceWeaponPFBullet(oWarrior, oEventCB, 9094, (lambda *a: Func686(*a, **{
'iPerform': 9094,
'sAttr': 'PFBulletRecover' })), 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9094, 1, -1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, -3000, 0, DAM_TYPE_WEAPON, '')


class CPerform(CCustomPerform):
    m_SID = 4290
    m_Name = '六方扣弹加专属弹'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'AttackCnt': 0 }
    m_DieDisable = 0

