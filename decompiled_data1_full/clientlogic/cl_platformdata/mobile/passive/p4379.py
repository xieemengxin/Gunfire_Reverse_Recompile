# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4379.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4379.pyc
# Source Generated with Decompyle++
# File: p4379.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39023, 'buildatk', 10, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39029, 'buildatk', 5, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39025, 'buildatk', 25, None)


class CPerform(CCustomPerform):
    m_SID = 4379
    m_Name = '【诡谲雪山】罗睺-落石受伤优化'
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

