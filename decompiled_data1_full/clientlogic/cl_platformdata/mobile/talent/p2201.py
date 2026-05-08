# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2201.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2201.pyc
# Source Generated with Decompyle++
# File: p2201.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Radius', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'ColdTime', -2000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Radius', 0, 4)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'ColdTime', -4000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'Radius', 0, 6)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1304, 'ColdTime', -6000, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, 1):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (0, (339, 2000, 0), ((339,), (lambda a0: a0 * 2000 + 0))), DAM_TYPE_PERFORM)


class CPerform(CCustomPerform):
    m_SID = 2201
    m_Name = '巨型爆破'
    m_MaxLevel = 3
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0

