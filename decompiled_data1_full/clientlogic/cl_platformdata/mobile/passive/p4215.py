# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4215.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4215.pyc
# Source Generated with Decompyle++
# File: p4215.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32504, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32505, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32506, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32507, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32534, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32505, 2)


class CPerform(CCustomPerform):
    m_SID = 4215
    m_Name = '改版桃被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

