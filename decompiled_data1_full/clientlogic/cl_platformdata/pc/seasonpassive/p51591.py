# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51591.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51591.pyc
# Source Generated with Decompyle++
# File: p51591.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func530, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubCD', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12042, 1, 0):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func530(*a))) > 0:
            cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func717(*a, **{
'sArg': 'SubCD' })))
        elif not cl_evcon.CheckHasState(oWarrior, oEventCB, 33958):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33958, 500, {
                'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })) }, 1, 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33958, 1, 500)


class CPerform(CCustomPerform):
    m_SID = 51591
    m_Name = '#NT#雷刃-E'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

