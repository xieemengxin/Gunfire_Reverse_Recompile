# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4060.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4060.pyc
# Source Generated with Decompyle++
# File: p4060.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('NeverShow') == 0:
        cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7942, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4060
    m_Name = '隐身怪阶段1显形'
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

