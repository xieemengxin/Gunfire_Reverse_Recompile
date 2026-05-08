# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15075.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15075.pyc
# Source Generated with Decompyle++
# File: p15075.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, -1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 4362, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 4362)


class CPerform(CCustomPerform):
    m_SID = 15075
    m_Name = '究极进化'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

