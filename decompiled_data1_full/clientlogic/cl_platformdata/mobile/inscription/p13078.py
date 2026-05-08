# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13078.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13078.pyc
# Source Generated with Decompyle++
# File: p13078.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_NOFIRE, INSCRIPTION_TYPE_NORMAL, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, PF_TYPE_CAREERPF, PF_TYPE_THROW, WEAPON_MINOR_PERFORM
from cl_newformula import Func547

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33270, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_NOFIRE, 2, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_NOFIRE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, 33270, 1)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33270, 1, 1) >= 5:
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33270, 0, None)
        cl_action.CommonAddSourceWeaponPFBulletByType(oWarrior, oEventCB.GetCBLifeCycle(), WEAPON_MINOR_PERFORM, (lambda *a: 0.3 * Func547(*a, **{
'sAttr': 'MaxPFBullet' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0) or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBAddEqualSouceWeaponStateCount(oWarrior, oEventCB, 33270, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33270, 1, 1) >= 5:
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33270, 0, None)
            cl_action.CommonAddSourceWeaponPFBulletByType(oWarrior, oEventCB.GetCBLifeCycle(), WEAPON_MINOR_PERFORM, (lambda *a: 0.3 * Func547(*a, **{
'sAttr': 'MaxPFBullet' })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 13078
    m_Name = '法杖专属词条2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_NORMAL
    m_ElementType = None
    m_LimitList = ((23, 24), (), ())
    m_ExcludeList = ((), (), (1704, 1709))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

