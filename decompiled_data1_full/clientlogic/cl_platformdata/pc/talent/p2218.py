# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2218.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2218.pyc
# Source Generated with Decompyle++
# File: p2218.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CONSHOOT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT) or cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 4, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)
    else:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 4:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 4, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 4:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT) or cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 3, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)
    else:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 3:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 3, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 3:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32231, 500, { }, 0, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT) or cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 2, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32232, 1000, { }, 0, None)
    else:
        cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 2:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32232, 1000, { }, 0, None)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckFixedTimeDamCnt(oWarrior, oEventCB, PF_TYPE_CONSHOOT, 500, 2, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32232, 1000, { }, 0, None)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 0)
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt') >= 2:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32232, 1000, { }, 0, None)


class CPerform(CCustomPerform):
    m_SID = 2218
    m_Name = '乘势追击'
    m_MaxLevel = 3
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0

