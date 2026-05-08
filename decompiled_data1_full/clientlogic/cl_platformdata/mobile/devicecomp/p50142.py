# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/devicecomp/p50142.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/devicecomp/p50142.pyc
# Source Generated with Decompyle++
# File: p50142.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import DEVICECOMP_TYPE_DEVICE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDisableDevicePF(oWarrior, oLifeCycle, 50361)
    cl_action.CommonAddPlayerDevicePerform(oWarrior, oLifeCycle, 50364)


class CPerform(CCustomPerform):
    m_SID = 50142
    m_Name = '天幕'
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
    m_ExclusiveDevice = (1003,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50140, 50141)
    m_DropShape = 5560
    m_DeployActive = 0
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

