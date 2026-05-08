# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2038.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2038.pyc
# Source Generated with Decompyle++
# File: p2038.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Att', 10000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Att', 15000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 10)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32038, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Att', 20000, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1409, 0, 0) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func308(*a) * 15 + 15)):
        cl_evact.EventReduceBulletUse(oWarrior, oEventCB, 1011)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32038, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 2038
    m_Name = '手雷大师'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 101

