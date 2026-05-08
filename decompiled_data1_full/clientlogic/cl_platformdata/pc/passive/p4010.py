# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4010.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4010.pyc
# Source Generated with Decompyle++
# File: p4010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'SkillAllCrazy', 2, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'SkillAllCrazy', -1, 0)
        cl_evact.EventCBRecordHitCartoon(oWarrior, oEventCB, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'SkillAllCrazy', None) <= 0 and cl_evcon.CheckBulletHitCount(oWarrior, oEventCB) == 2:
        cl_evact.PassiveFillBullet(oWarrior, oEventCB, 2, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'SkillAllCrazy', None) > 0:
        cl_evact.PassiveFillBullet(oWarrior, oEventCB, 2, 0)


class CPerform(CCustomPerform):
    m_SID = 4010
    m_Name = '1502全爆头回子弹'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

