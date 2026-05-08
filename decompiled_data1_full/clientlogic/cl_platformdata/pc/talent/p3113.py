# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3113.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3113.pyc
# Source Generated with Decompyle++
# File: p3113.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM
from cl_newformula import Func308, Func540

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1316, 'Att', 12000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1318, 'Att', 12000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1316, 'Att', 24000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1318, 'Att', 24000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1316, 'Att', 36000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1318, 'Att', 36000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1316: 1,
        1318: 1,
        1712: 1 }, 0, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func540(*a) * Func308(*a)), 0, DAM_TYPE_PERFORM, None, None)


class CPerform(CCustomPerform):
    m_SID = 3113
    m_Name = '燎原烈火'
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
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 112

