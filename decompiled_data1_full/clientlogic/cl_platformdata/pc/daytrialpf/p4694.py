# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4694.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4694.pyc
# Source Generated with Decompyle++
# File: p4694.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-4692Intensify', 0, 1)
    cl_evact.PassiveCBChangeSceneData(oWarrior, oEventCB, 'PF-4692Intensify', -1, 0)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1317, cl_evact.PassiveCBGetSceneData(oWarrior, oEventCB, 'PF-4692Intensify'))


class CPerform(CCustomPerform):
    m_SID = 4694
    m_Name = '清除4692的状态层数'
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

