# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5034.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5034.pyc
# Source Generated with Decompyle++
# File: p5034.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1429, 'Pierce', 3)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1429, 'Radius', 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 5034
    m_Name = '三重霜冻'
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
    m_TalentType = 2
    m_IsRareTalent = 1
    m_Career = 116

