# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13529.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13529.pyc
# Source Generated with Decompyle++
# File: p13529.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF
from cl_newformula import Func340, Func540

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'pf13730', None, None)
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32682):
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 50 * Func340(*a, **{
'sKey': 'pf13730' })), 0)
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf13730', None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func540(*a))) >= 3000:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32740, 9000, { }, 1, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 32740, 1, 0, 0, 9000)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf13529', None, None, None)


class CPerform(CCustomPerform):
    m_SID = 13529
    m_Name = '怒焰奔腾'
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
    m_Career = 112

