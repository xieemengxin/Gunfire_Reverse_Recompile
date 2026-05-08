# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5426.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5426.pyc
# Source Generated with Decompyle++
# File: p5426.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func208, Func525

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMADDBULLET, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func525(*a))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func208(*a))):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32822, 400, { }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func525(*a))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func208(*a))):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32822, 600, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5426
    m_Name = '快枪巧手'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 114

