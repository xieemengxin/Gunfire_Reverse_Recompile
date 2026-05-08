# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2210.pyc
# Source Generated with Decompyle++
# File: p2210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32217, 0, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32217, (lambda *a: Func410(*a, **{
'sid': 32683 }) * 5), None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32683, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32683, (lambda *a: Func410(*a, **{
'sid': 32217 }) * 0.2), None)


class CPerform(CCustomPerform):
    m_SID = 2210
    m_Name = '残羹盛宴'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 103

