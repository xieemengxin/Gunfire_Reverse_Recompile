# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3319.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3319.pyc
# Source Generated with Decompyle++
# File: p3319.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32919, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33901, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1426: 1 }, 1, 0):
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32810):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32810, 0, { }, 1, 0, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 33903):
            cl_evact.PassiveCBRemoveStateFromSelf(oWarrior, oEventCB, 33903)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33902, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), {
            'SubCount': (lambda *a: Func717(*a, **{
'sArg': 'SubCount' })),
            'IntervalTime': (lambda *a: Func717(*a, **{
'sArg': 'IntervalTime' })) }, 1, 0, 0)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33901, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })), 0)


class CPerform(CCustomPerform):
    m_SID = 3319
    m_Name = '极致改装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'EffectTime': 80,
        'AddCount': 5,
        'SubCount': 4,
        'IntervalTime': 20 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 0

