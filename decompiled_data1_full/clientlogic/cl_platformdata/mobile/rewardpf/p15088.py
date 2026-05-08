# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15088.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15088.pyc
# Source Generated with Decompyle++
# File: p15088.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1915, 'Att', 50, 1)


class CPerform(CCustomPerform):
    m_SID = 15088
    m_Name = '#NT#武器灵佑'
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

