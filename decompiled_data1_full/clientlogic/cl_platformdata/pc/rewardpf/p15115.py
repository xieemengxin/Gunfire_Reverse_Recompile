# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15115.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15115.pyc
# Source Generated with Decompyle++
# File: p15115.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_ADD, HP_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, HP_RADIO_ADD, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, HP_RADIO_SUB, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) == 100 or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HPInfo') != 1:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HPInfo', 1)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33421, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33420, 0, { }, 1)
    elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HPInfo') != 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HPInfo', 2)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33420, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33421, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 15115
    m_Name = '#NT#进退自如'
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

