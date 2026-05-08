# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5372.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5372.pyc
# Source Generated with Decompyle++
# File: p5372.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, STATE_CLS_ABNORMAL, WARRIOR_BUILD_TRAP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP) or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1060):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    else:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -7000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 1009)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1009, 0, { }, 1)
    cl_action.CommonRemoveAllStateByType(oWarrior, oEventCB.GetCBLifeCycle(), STATE_CLS_ABNORMAL)


class CPerform(CCustomPerform):
    m_SID = 5372
    m_Name = '#NT#天袭分身被动'
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

