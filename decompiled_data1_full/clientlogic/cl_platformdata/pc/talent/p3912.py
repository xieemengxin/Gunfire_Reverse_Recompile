# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3912.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3912.pyc
# Source Generated with Decompyle++
# File: p3912.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1436, 'Spread', 1, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1436, 'AddCanAimMonsterState', 1, 1)


class CPerform(CCustomPerform):
    m_SID = 3912
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 120

