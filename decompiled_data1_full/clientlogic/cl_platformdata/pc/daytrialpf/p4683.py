# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p4683.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p4683.pyc
# Source Generated with Decompyle++
# File: p4683.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 1, 0, 6)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) and cl_evcon.GetTargetStateNum(oWarrior, oEventCB, 1299, 0) < 3 and not cl_evcon.CheckHasState(oWarrior, oEventCB, 1009):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1299, 0, { }, 0, 0, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateNum(oWarrior, oEventCB, 1299, 0) >= 3:
        cl_evact.EventChangeHP(oWarrior, oEventCB, 1)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1300, 0, { }, 1, 0, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1299, 0)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4683
    m_Name = '怪物受爆炸3次修改属性'
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

