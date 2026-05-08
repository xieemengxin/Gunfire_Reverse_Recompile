# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51655.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51655.pyc
# Source Generated with Decompyle++
# File: p51655.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func535, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 100)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 200)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 300)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 400)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Cnt', (lambda *a: Func535(*a)))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cnt') > 0:
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 39707):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39707, 500, {
                'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 1, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Cnt') > 0:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39707, (lambda *a: Func717(*a, **{
'sArg': 'Cnt' })), 500)


class CPerform(CCustomPerform):
    m_SID = 51655
    m_Name = '回复增伤'
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

