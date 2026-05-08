# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4051.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4051.pyc
# Source Generated with Decompyle++
# File: p4051.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7914, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7055, 0, { }, 0)


class CPerform(CCustomPerform):
    m_SID = 4051
    m_Name = '毒系自爆怪被动'
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

