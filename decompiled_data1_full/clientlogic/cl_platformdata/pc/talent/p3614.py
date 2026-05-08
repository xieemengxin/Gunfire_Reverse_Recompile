# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3614.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3614.pyc
# Source Generated with Decompyle++
# File: p3614.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 5, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33097):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func308(*a) + 3000), 0, 0, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 15 * Func308(*a) + 15))
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 8, 0, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func308(*a) + 3000), 0, 0, '')
        else:
            cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 15 * Func308(*a) + 15))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33097) or cl_evcon.CheckHasState(oWarrior, oEventCB, 33040):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func308(*a) + 3000), 0, 0, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 15 * Func308(*a) + 15))
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 8, 0, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 3000 * Func308(*a) + 3000), 0, 0, '')
        else:
            cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: 15 * Func308(*a) + 15))


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33097):
        cl_evact.EventCBSkillCopyWeaponTrajectoryDamage(oWarrior, oEventCB, (lambda *a: 1000 * (Func308(*a) + 0)), 0, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33097) or cl_evcon.CheckHasState(oWarrior, oEventCB, 33040):
        cl_evact.EventCBSkillCopyWeaponTrajectoryDamage(oWarrior, oEventCB, 3000, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3614
    m_Name = '远绘近染'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

