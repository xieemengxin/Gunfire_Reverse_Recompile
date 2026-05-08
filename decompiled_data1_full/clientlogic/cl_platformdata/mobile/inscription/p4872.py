# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4872.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4872.pyc
# Source Generated with Decompyle++
# File: p4872.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4870', None) >= 2:
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 10000)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectHitNumInfo(oWarrior, oEventCB, 'p4870')


class CPerform(CCustomPerform):
    m_SID = 4872
    m_Name = '效率至上'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((2,), (), ())
    m_ExcludeList = ((), (4870,), (1211, 1416, 1107))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

