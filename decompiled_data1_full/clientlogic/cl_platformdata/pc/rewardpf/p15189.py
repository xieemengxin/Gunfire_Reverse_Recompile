# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15189.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15189.pyc
# Source Generated with Decompyle++
# File: p15189.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33487, 600, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15189
    m_Name = '从容不迫'
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

