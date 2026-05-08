# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3909.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3909.pyc
# Source Generated with Decompyle++
# File: p3909.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'StateTriggerInterval', 80, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'NotReduceRatio', 30, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'StateTriggerInterval', 60, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'NotReduceRatio', 50, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'StateTriggerInterval', 40, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1436, 'NotReduceRatio', 70, 1)


class CPerform(CCustomPerform):
    m_SID = 3909
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 120

