# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p40074.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p40074.pyc
# Source Generated with Decompyle++
# File: p40074.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSavedData(oWarrior, oLifeCycle, 'ExtraReceiveTaskNum', 1)
    cl_action.CommonAddSavedData(oWarrior, oLifeCycle, 'TaskRefreshTimes', 2)


class CPerform(CCustomPerform):
    m_SID = 40074
    m_Name = '天降大任-犹豫不决2奖励'
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

