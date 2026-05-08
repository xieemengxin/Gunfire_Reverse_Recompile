# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51901.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51901.pyc
# Source Generated with Decompyle++
# File: p51901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 100)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 10)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 100)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 200)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 20)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 100)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 400)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 40)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 100)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_InitValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtraValue', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51901_ExtendTime', 0)


class CPerform(CCustomPerform):
    m_SID = 51901
    m_Name = '临时护盾'
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

