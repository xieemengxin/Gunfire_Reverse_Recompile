# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3308.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3308.pyc
# Source Generated with Decompyle++
# File: p3308.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Att', 20000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8009, 'Att', 20000, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Att', 40000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8009, 'Att', 40000, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Att', 60000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Radius', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8009, 'Att', 60000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8009, 'Radius', 0, 2)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 5356, (lambda *a: Func308(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetRemovePerform(oWarrior, oEventCB, 5356)


class CPerform(CCustomPerform):
    m_SID = 3308
    m_Name = '高热核心'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 114

