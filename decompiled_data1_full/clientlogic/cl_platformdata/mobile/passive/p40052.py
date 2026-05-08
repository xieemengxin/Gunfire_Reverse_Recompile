# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p40052.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p40052.pyc
# Source Generated with Decompyle++
# File: p40052.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 32936):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 32936, 30, None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32936, 0, {
            'StateCount': 30 }, 1)


class CPerform(CCustomPerform):
    m_SID = 40052
    m_Name = '天降大任-迅捷如风3奖励'
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

