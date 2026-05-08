# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15065.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15065.pyc
# Source Generated with Decompyle++
# File: p15065.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33688, 2, 'AdditionRatio')


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateStatistics(oWarrior, oLifeCycle, 33688, -2, 'AdditionRatio')


class CPerform(CCustomPerform):
    m_SID = 15065
    m_Name = '武器宗师'
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

