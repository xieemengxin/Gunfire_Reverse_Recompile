# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3616.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3616.pyc
# Source Generated with Decompyle++
# File: p3616.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF
from cl_newformula import Func308, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'TriggerCount', 5, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'MaxCount', 4, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'TriggerCount', 4, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'MaxCount', 4, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'TriggerCount', 3, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3616, 'MaxCount', 5, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33100, 1, 0) <= 0:
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 33100)
    if cl_evcon.CheckTargetInInkArea(oWarrior, oEventCB) and cl_condition.GetStateStatistics(oWarrior, oEventCB.GetCBLifeCycle(), 33100, 'InVirtual') == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurCount', 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CurCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TriggerCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurCount', 0)
            if cl_evcon.CheckHasState(oWarrior, oEventCB, 33100):
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33100, 1, 0)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33100, 0, {
                    'MaxCount': (lambda *a: Func361(*a, **{
'sid': 3616,
'sArgs': 'MaxCount' })) }, 1, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 33100, 1, 0) > 2:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: 4000 * Func308(*a)), 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 3616
    m_Name = '浴墨蚀心'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'MaxCount': 4 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 117

