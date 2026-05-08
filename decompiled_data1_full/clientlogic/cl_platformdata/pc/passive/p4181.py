# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4181.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4181.pyc
# Source Generated with Decompyle++
# File: p4181.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32289, 0, 0, None):
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 800, 0, 1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32289, 8000, { }, 1, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonWaitEndUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 39160, 32289)


class CPerform(CCustomPerform):
    m_SID = 4181
    m_Name = '瞬移被动'
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

