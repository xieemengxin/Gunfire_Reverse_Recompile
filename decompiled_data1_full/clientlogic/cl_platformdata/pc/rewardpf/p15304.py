# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15304.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15304.pyc
# Source Generated with Decompyle++
# File: p15304.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33838, 4, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33766):
        cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'ExplodeDelay', 0, 25)
        cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'ExplodeDelay', 0, 25)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 33838, -4, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33766):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 25)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'ExplodeDelay', 0, 25)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33766):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 'ExplodeDelay', 0, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'ExplodeDelay', 0, 0)


class CPerform(CCustomPerform):
    m_SID = 15304
    m_Name = '无双战意'
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

