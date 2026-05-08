# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15099.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15099.pyc
# Source Generated with Decompyle++
# File: p15099.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 15099, '33124MaxCount', 36, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 15099, '33124Return', 30, None)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33124, { }, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 33124, 24, 1, None)


class CPerform(CCustomPerform):
    m_SID = 15099
    m_Name = '染墨生辉'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

