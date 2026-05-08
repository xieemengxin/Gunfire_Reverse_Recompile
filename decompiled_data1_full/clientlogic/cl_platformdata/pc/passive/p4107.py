# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4107.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4107.pyc
# Source Generated with Decompyle++
# File: p4107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7079, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7082, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 4107
    m_Name = '火箭炮兵被动初始炮管可用'
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

