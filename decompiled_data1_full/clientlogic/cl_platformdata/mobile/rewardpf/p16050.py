# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16050.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16050.pyc
# Source Generated with Decompyle++
# File: p16050.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UPGRADE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 100)


class CPerform(CCustomPerform):
    m_SID = 16050
    m_Name = '天外横财'
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

