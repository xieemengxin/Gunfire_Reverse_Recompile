# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4341.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4341.pyc
# Source Generated with Decompyle++
# File: p4341.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7149)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7149)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7149)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'Att', 0, 5000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'MaxCover', 0, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'ColdTime', 0, -150)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7149)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7149)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'Att', 0, 10000)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'MaxCover', 0, 2)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 7149, 'ColdTime', 0, -300)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 7149)


class CPerform(CCustomPerform):
    m_SID = 4341
    m_Name = '御灵师仆从E3'
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

