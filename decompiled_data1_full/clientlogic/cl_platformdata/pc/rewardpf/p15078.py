# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15078.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15078.pyc
# Source Generated with Decompyle++
# File: p15078.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 32854, 100, 'ExTime')


class CPerform(CCustomPerform):
    m_SID = 15078
    m_Name = '开山破浪'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

