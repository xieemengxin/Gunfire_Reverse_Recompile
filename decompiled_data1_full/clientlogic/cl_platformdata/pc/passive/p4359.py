# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4359.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4359.pyc
# Source Generated with Decompyle++
# File: p4359.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import TYPE_RELIFE_RESCUE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32898, 100, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_RESCUE) or cl_condition.CommonCheckTargetDeadReason(oWarrior, oEventCB.GetCBLifeCycle(), 'PF13540'):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32898, 100, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4359
    m_Name = '御灵师仆从出生被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

