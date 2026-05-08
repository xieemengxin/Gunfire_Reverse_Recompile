# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14609.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14609.pyc
# Source Generated with Decompyle++
# File: p14609.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_NORLARGESUMMON
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckTargetFightType(oWarrior, oLifeCycle, WARRIOR_NORLARGESUMMON):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurVal', (lambda *a: Func717(*a, **{
'sArg': 'MinorVal' })))
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'ChallengeLv' }))) < 5 or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurVal') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectVal'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurVal', 0)
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TriggerTimes', 1)
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TriggerTimes') >= 3:
                cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_START, -1)
            cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1976, 0, { })
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurVal') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EffectVal'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurVal', -20)
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TriggerTimes', 1)
            if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TriggerTimes') >= 3:
                cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_START, -1)
            cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1976, 0, { })


class CPerform(CCustomPerform):
    m_SID = 14609
    m_Name = '骰子挑战4技能'
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
        'EffectVal': 0,
        'CurVal': 0,
        'TriggerTimes': 0 }
    m_DieDisable = 0

