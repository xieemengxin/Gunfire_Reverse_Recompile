# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14007.pyc
# Source Generated with Decompyle++
# File: p14007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 4063)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 7111, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 7052, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7136, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4063, 3, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 4063, 3, None, None)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7136, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 14007
    m_Name = '轮回9-流寇纵火者'
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

