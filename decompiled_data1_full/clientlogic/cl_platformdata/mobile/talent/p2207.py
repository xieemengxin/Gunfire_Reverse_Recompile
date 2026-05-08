# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2207.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2207.pyc
# Source Generated with Decompyle++
# File: p2207.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, PF_TYPE_THROW
from cl_newformula import Func339

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1411, 'Radius', 0, 2)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1411, 'Radius', 0, 3)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1411, 'Radius', 0, 5)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func339(*a) * 2000 + 0), 0, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func339(*a) * 3000 + 0), 0, DAM_TYPE_PERFORM, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func339(*a) * 4000 + 0), 0, DAM_TYPE_PERFORM, None, None)


class CPerform(CCustomPerform):
    m_SID = 2207
    m_Name = '绝对优势'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 103

