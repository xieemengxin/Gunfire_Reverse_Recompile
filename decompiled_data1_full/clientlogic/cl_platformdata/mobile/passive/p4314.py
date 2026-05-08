# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4314.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4314.pyc
# Source Generated with Decompyle++
# File: p4314.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetDieRemoveDelay(oWarrior, oLifeCycle, 4)


class CPerform(CCustomPerform):
    m_SID = 4314
    m_Name = '罗睺-阶段一弱点被动'
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

