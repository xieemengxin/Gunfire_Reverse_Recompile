# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4093.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4093.pyc
# Source Generated with Decompyle++
# File: p4093.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 4092)
    cl_action.CommonEnablePerform(oWarrior, oLifeCycle, 4089)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 61, 0, None, None)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF4356', 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'PF4356', 0)


class CPerform(CCustomPerform):
    m_SID = 4093
    m_Name = '三幕Boss阶段4'
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

