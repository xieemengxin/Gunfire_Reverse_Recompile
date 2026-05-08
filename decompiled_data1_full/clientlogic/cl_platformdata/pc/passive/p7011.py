# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p7011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p7011.pyc
# Source Generated with Decompyle++
# File: p7011.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 20, 20, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (0, None, ((304, 'RDeviceEnergy'), (lambda a0: a0 / 5))), 0)


class CPerform(CCustomPerform):
    m_SID = 7011
    m_Name = '装置自动回复能量'
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
    m_DieDisable = 1

