# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15109.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15109.pyc
# Source Generated with Decompyle++
# File: p15109.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonUpdateStateCountEff(oWarrior, oLifeCycle, 150)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonUpdateStateCountEff(oWarrior, oLifeCycle, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonUpdateStateCountEff(oWarrior, oLifeCycle, 200)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonUpdateStateCountEff(oWarrior, oLifeCycle, 0)


class CPerform(CCustomPerform):
    m_SID = 15109
    m_Name = '#NT#提升计数套装'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

