# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15194.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15194.pyc
# Source Generated with Decompyle++
# File: p15194.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func535

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33497, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cnt', (lambda *a: Func535(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cnt') > 0:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33497, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt'), 500)


class CPerform(CCustomPerform):
    m_SID = 15194
    m_Name = '次要冷却'
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

