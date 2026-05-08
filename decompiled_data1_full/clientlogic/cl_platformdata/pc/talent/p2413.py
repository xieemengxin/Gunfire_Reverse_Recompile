# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2413.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2413.pyc
# Source Generated with Decompyle++
# File: p2413.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_LASER, PF_TYPE_CONSHOOT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2413', None) == 0 and not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32473):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2413', 1, None)
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 20, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None) and cl_evcon.CheckWeaponType(oWarrior, oEventCB, EQUIP_LASER) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'pf2413', None) == 1:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf2413', -1, None)


class CPerform(CCustomPerform):
    m_SID = 2413
    m_Name = '无尽之怒'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 105

