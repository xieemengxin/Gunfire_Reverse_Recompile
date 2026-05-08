# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4484.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4484.pyc
# Source Generated with Decompyle++
# File: p4484.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Trajectory', 0, 0, 0, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4484', None) >= 2 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4484', None) <= 3:
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Trajectory', 100, 0, 0, { })
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4484', None) == 4:
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Trajectory', 200, 0, 0, { })
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4484', None) == 5:
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Trajectory', 300, 0, 0, { })
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4484', None) >= 6:
        cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Trajectory', 400, 0, 0, { })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB):
        cl_evact.PassiveCBSetCollectHitNumInfo(oWarrior, oEventCB, 'p4484')


class CPerform(CCustomPerform):
    m_SID = 4484
    m_Name = '单次爆炸'
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

