# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p5421.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p5421.pyc
# Source Generated with Decompyle++
# File: p5421.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32629, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32687, 0, { }, 0)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32629, (lambda *a: Func410(*a, **{
'sid': 32687 })), None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32687, (lambda *a: Func410(*a, **{
'sid': 32629 })), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32629, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32687, 0, { }, 0)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32629, (lambda *a: Func410(*a, **{
'sid': 32687 })), None)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32687, (lambda *a: Func410(*a, **{
'sid': 32629 })), None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32630, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32687, 0, { }, 0)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32630, (lambda *a: Func410(*a, **{
'sid': 32687 })), None)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 32687, (lambda *a: Func410(*a, **{
'sid': 32630 })), None)


class CPerform(CCustomPerform):
    m_SID = 5421
    m_Name = '真气护体'
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
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 111

