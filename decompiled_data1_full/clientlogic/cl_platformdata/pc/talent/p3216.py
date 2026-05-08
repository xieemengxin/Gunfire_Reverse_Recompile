# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3216.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3216.pyc
# Source Generated with Decompyle++
# File: p3216.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func560, Func561
from cl_commondefines import GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 3, 0, 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 0, 100, 2)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanCount') >= 1 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func561(*a))) == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CanCount', -1)
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func560(*a))):
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 2, GAMBLER_REPLACE_DEFAULT, 0)
        else:
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CanCount', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanCount') >= 1 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func561(*a))) == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CanCount', -1)
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func560(*a))):
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 2, GAMBLER_REPLACE_DEFAULT, 0)
        else:
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanCount') >= 1 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func561(*a))) == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CanCount', -1)
        if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func560(*a))):
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 2, GAMBLER_REPLACE_DEFAULT, 1)
        else:
            cl_action.CommonAppendQuality(oWarrior, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 1, 1, GAMBLER_REPLACE_DEFAULT, 1)


class CPerform(CCustomPerform):
    m_SID = 3216
    m_Name = '奇妙弹夹'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 113

