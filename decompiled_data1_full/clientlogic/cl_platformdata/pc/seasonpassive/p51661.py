# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51661.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51661.pyc
# Source Generated with Decompyle++
# File: p51661.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDRatio', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 700)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDRatio', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedAddRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDRatio', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39718, 1, 0, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39718, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), {
            'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
            'SpeedAddRatio': (lambda *a: Func717(*a, **{
'sArg': 'SpeedAddRatio' })),
            'EffectTime': (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })),
            'CDRatio': (lambda *a: Func717(*a, **{
'sArg': 'CDRatio' })) }, 1, -1, 0)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39718, 1, 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })))


class CPerform(CCustomPerform):
    m_SID = 51661
    m_Name = '#NT#疾步如飞'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

