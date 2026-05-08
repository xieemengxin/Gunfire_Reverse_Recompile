# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2912.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2912.pyc
# Source Generated with Decompyle++
# File: p2912.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) + 5), None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) - 5), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) + 10), None)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) - 10), None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) + 25), None)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'BaseEnergyNum' }) - 25), None)


class CPerform(CCustomPerform):
    m_SID = 2912
    m_Name = '霸道寸劲'
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
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 110

