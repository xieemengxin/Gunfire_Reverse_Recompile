# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3007.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3007.pyc
# Source Generated with Decompyle++
# File: p3007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, PF_TYPE_THROW, SWORD_DOUBLE_DAMAGE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1422, 'Att', 15000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1422, 'Att', 30000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1422, 'Att', 45000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if (cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1709, 1, 0)) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 25):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 10000, DAM_TYPE_PERFORM, '')
        cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, SWORD_DOUBLE_DAMAGE)


class CPerform(CCustomPerform):
    m_SID = 3007
    m_Name = '魂飞魄散'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 111

