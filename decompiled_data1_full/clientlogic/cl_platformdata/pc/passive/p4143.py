# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4143.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4143.pyc
# Source Generated with Decompyle++
# File: p4143.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func378, Func738

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 5)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddRoomChallengeCollectDataFromMonster(oWarrior, oLifeCycle, 'Count', -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func378(*a))) <= 0:
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE_BEFORE, -1)
        cl_evact.EventCBTriggerKillEffect(oWarrior, oEventCB)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oWarrior, oEventCB, 1)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1206, (lambda *a: max(50, 300 - max(0, Func738(*a, **{
'sKey': 'Count' }) - 5) * 30)), { }, 0, 1, 0)
        cl_action.CommonAddRoomChallengeCollectDataFromMonster(oWarrior, oEventCB.GetCBLifeCycle(), 'Count', 1)
        cl_evact.EventCBAddTargetCustomData(oWarrior, oEventCB, 'DelayedDeath', 1)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4143
    m_Name = '战场热诚'
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
    m_DieDisable = 1

