# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3101.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3101.pyc
# Source Generated with Decompyle++
# File: p3101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1423, 'Att', 10000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8007, 'Att', 10000, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1423, 'Att', 20000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8007, 'Att', 20000, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1423, 'Att', (lambda *a: 30000 + Func304(*a, **{
'sAttr': 'EnergyMax' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 8007, 'Att', (lambda *a: 30000 + Func304(*a, **{
'sAttr': 'EnergyMax' })), 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'EnergyMax', -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1423, 'Att', (lambda *a: 30000 + Func304(*a, **{
'sAttr': 'EnergyMax' })), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 8007, 'Att', (lambda *a: 30000 + Func304(*a, **{
'sAttr': 'EnergyMax' })), 0)


class CPerform(CCustomPerform):
    m_SID = 3101
    m_Name = '灵能火陨'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 112

