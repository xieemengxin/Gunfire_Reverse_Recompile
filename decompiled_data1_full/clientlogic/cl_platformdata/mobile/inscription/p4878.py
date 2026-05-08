# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p4878.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p4878.pyc
# Source Generated with Decompyle++
# File: p4878.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponBulletCnt(oWarrior, oEventCB, 2):
        cl_evact.PassiveFillBullet(oWarrior, oEventCB, 1, 0)
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'pf4878', 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1177, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf4878', None) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1177, 0, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4878
    m_Name = '迷你弹夹'
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
    m_ItemAttr = {
        'MaxBullet': (0, 0, 2) }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1304, 1305, 1306, 1401, 1404, 1406, 1407, 1501, 1503, 1507, 1310, 1302, 1513, 1804, 1205, 1315, 1316), ())
    m_ExcludeList = ((), (4802, 4842, 4849, 4850, 4851, 4819, 13073, 4859, 13051), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

