# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3412.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3412.pyc
# Source Generated with Decompyle++
# File: p3412.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 + 5))))


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 - 5))))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 + 10))))


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 - 10))))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 + 20))))


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 4347, 'BaseEnergyNum', (0, None, ((361, 4347, 'BaseEnergyNum'), (lambda a0: a0 - 20))))


class CPerform(CCustomPerform):
    m_SID = 3412
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
    m_Career = 115

