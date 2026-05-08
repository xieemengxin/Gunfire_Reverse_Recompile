# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4346.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4346.pyc
# Source Generated with Decompyle++
# File: p4346.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PATHMODE_COLLISIONLESS

def Action1(oWarrior, oLifeCycle):
    cl_action.SwitchTargetPathMode(oWarrior, oLifeCycle, PATHMODE_COLLISIONLESS)


class CPerform(CCustomPerform):
    m_SID = 4346
    m_Name = '御灵师仆从炮台型被动'
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

