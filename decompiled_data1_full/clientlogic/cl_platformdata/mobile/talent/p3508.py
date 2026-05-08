# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3508.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3508.pyc
# Source Generated with Decompyle++
# File: p3508.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import FLAW_COLDTIME, FLAW_MAXCOUNT, FLAW_SIZE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_SIZE, 0, 1000, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_COLDTIME, 0, -2500, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_SIZE, 0, 2000, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_COLDTIME, 0, -5000, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_MAXCOUNT, 10000, 0, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_SIZE, 0, 3000, 1)
    cl_action.CommonAddFlawAddition(oWarrior, oLifeCycle, FLAW_COLDTIME, 0, -7500, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonReduceCurFlawCD(oWarrior, oEventCB.GetCBLifeCycle(), 20, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_action.CommonReduceCurFlawCD(oWarrior, oEventCB.GetCBLifeCycle(), 0, 50)
    else:
        cl_action.CommonReduceCurFlawCD(oWarrior, oEventCB.GetCBLifeCycle(), 40, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckBreakFlaw(oWarrior, oEventCB, None):
        cl_action.CommonReduceCurFlawCD(oWarrior, oEventCB.GetCBLifeCycle(), 0, 100)
    else:
        cl_action.CommonReduceCurFlawCD(oWarrior, oEventCB.GetCBLifeCycle(), 60, 0)


class CPerform(CCustomPerform):
    m_SID = 3508
    m_Name = '寒眸洞烛'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 116

