# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5335.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5335.pyc
# Source Generated with Decompyle++
# File: p5335.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 40, 40, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1993, 0, { })


class CPerform(CCustomPerform):
    m_SID = 5335
    m_Name = '电柱使用技能'
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

