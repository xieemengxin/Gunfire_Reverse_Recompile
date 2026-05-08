# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51623.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51623.pyc
# Source Generated with Decompyle++
# File: p51623.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func535

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33567, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 160, 160, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33567, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 120, 120, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33567, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 80, 80, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33567, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 40, 40, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33567, 0, { }, 1)
    cl_action.CommonAddPerformCDTimer(oWarrior, oLifeCycle, 50, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cnt', (lambda *a: Func535(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cnt') > 0:
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33567, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Cnt'), 300)


class CPerform(CCustomPerform):
    m_SID = 51623
    m_Name = '次要回复核心'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

