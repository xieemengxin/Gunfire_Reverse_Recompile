# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3408.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3408.pyc
# Source Generated with Decompyle++
# File: p3408.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5811) and cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((420,), (lambda a0: a0)))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32779, 0)
    else:
        cl_evact.PassiveExtBulletUse(oWarrior, oEventCB, (0, None, ((2, ((410, 32775), (lambda a0: a0 // 10)), 4), (lambda a0: a0))))
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32779, 0, { }, 1)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32805, 0, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1428, 1, None):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (0, None, ((2, ((410, 32775), (lambda a0: a0 // 10)), 4), (lambda a0: 4000 * a0))), DAM_TYPE_PERFORM)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (0, None, ((2, ((410, 32775), (lambda a0: a0 // 10)), 4), (lambda a0: 4000 * a0))), DAM_TYPE_PERFORM)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1427, 1, None) and cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32805, -1, None) != 0:
        cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, (0, None, ((410, 32805), (lambda a0: a0))))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1427, 1, None) and cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32805, -1, None) != 0:
        cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4508, (0, None, ((410, 32805), (lambda a0: a0))))


class CPerform(CCustomPerform):
    m_SID = 3408
    m_Name = '破浪一击'
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
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 115

