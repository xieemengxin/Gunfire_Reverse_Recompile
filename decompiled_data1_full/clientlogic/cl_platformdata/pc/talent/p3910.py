# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3910.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3910.pyc
# Source Generated with Decompyle++
# File: p3910.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_VICTIM, TRIGGER_PARASITIC
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseProbability', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDamFactor', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, TRIGGER_PARASITIC, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseProbability', 35)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDamFactor', 25)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, TRIGGER_PARASITIC, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseProbability', 45)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDamFactor', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, TRIGGER_PARASITIC, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func717(*a, **{
'sArg': 'BaseProbability' }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33867, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33867, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33867, 0, {
                'MaxCnt': (lambda *a: Func717(*a, **{
'sArg': 'MaxCnt' })),
                'AddDamFactor': (lambda *a: Func717(*a, **{
'sArg': 'AddDamFactor' })) }, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, 'pf3810', 0) == 0 and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'ParasiticCount') >= cl_evcon.EventCBGetTargetStateMaxCount(oWarrior, oEventCB, 33712, 1, 0):
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, 'pf3810', 400, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33873, 100, { }, 0, 1, 0)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func717(*a, **{
'sArg': 'BaseProbability' }))):
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33867, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33867, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33867, 0, {
                'MaxCnt': (lambda *a: Func717(*a, **{
'sArg': 'MaxCnt' })),
                'AddDamFactor': (lambda *a: Func717(*a, **{
'sArg': 'AddDamFactor' })) }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 3910
    m_Name = '#NT#觉醒占位'
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
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 120

