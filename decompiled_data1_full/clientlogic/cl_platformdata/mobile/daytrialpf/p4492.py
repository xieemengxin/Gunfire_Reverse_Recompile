# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p4492.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p4492.pyc
# Source Generated with Decompyle++
# File: p4492.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1672, 1, None):
        cl_evact.PassiveCBUsePerformWithKillMonster(oWarrior, oEventCB, 1672)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1672, 1, None):
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_TRUE)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 1361, None, None) == 1:
            cl_evact.PassiveCBUsePerformWithKillMonster(oWarrior, oEventCB, 1672)
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1361, 1, None, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1361, 0, { }, 0, 0, None)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1361, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 4492
    m_Name = '击杀敌人时，会额外造成一次大范围爆炸伤害'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

