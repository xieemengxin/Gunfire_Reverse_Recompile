# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15307.pyc
# Source Generated with Decompyle++
# File: p15307.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1436, 'ParasiticMul', 8000, 1)


class CPerform(CCustomPerform):
    m_SID = 15307
    m_Name = '#NT#生生不息'
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

