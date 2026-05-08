# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2217.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2217.pyc
# Source Generated with Decompyle++
# File: p2217.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1304, 0, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32470) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (0, None, ((304, 'Armor'), (lambda a0: a0 * 1.2))), 0, DAM_TYPE_PERFORM)
        cl_evact.EventChangeArmor(oWarrior, oEventCB, (0, None, ((304, 'Armor'), (lambda a0: -a0))))
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32470, 10, { }, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 2217
    m_Name = '孤注一掷'
    m_MaxLevel = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0

