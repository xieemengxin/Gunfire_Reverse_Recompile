# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4368.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4368.pyc
# Source Generated with Decompyle++
# File: p4368.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'SaveTime', 20000, 0, -1)
    cl_action.CommonAddDyingSecond(oWarrior, oLifeCycle, 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 4368
    m_Name = '喜欢躺平'
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

