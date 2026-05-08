# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3217.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3217.pyc
# Source Generated with Decompyle++
# File: p3217.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func560, Func563
from cl_commondefines import DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func563(*a) * 1000), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_MODIFY_GROOVENUM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func563(*a) * 2000), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_MODIFY_GROOVENUM, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func563(*a) * 3000), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_MODIFY_GROOVENUM, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func563(*a) * 1000), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32857) == 0:
        cl_evact.EventCBImmuneDamageByType(oWarrior, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32857, 1200, { }, 1, -1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func563(*a) * 2000), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32857) == 0:
        cl_evact.EventCBImmuneDamageByType(oWarrior, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32857, 1200, { }, 1, -1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func563(*a) * 3000), 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32857) == 0:
        cl_evact.EventCBImmuneDamageByType(oWarrior, oEventCB, DAM_MASK_ELEMENT, IMMUNITY_SHOWCOVER)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32857, 900, { }, 1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 3217
    m_Name = '星灵祝福'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 113

