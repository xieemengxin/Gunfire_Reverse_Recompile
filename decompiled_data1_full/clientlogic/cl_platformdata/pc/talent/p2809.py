# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2809.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2809.pyc
# Source Generated with Decompyle++
# File: p2809.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, -1500)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, -3000)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, -4500)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, 1500)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, 3000)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, 4500)


class CPerform(CCustomPerform):
    m_SID = 2809
    m_Name = '妖星B3'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 108

