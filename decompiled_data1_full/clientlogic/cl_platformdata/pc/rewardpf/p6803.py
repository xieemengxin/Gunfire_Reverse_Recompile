# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6803.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6803.pyc
# Source Generated with Decompyle++
# File: p6803.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 6951, 'DamReduction', 3, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 6951, 'DamReduction', 9, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 6951, 'DamReduction', 15, 1)


class CPerform(CCustomPerform):
    m_SID = 6803
    m_Name = '伤害抵抗（AI）'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

