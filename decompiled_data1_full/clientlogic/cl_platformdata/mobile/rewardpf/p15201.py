# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15201.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15201.pyc
# Source Generated with Decompyle++
# File: p15201.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ACTIVE_SENDMESSAGE, ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJECT_OWNER, OBJ_VICTIM
from cl_newformula import Func223, Func340, Func361, Func587, Func728, Func744

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8607)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, ACTIVE_SENDMESSAGE, 0, 0, 0)
    cl_action.CommonChangeMoveDis(oWarrior, oLifeCycle, '15201SuitRecord', 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    if cl_condition.CheckIsAIHero(oWarrior, oLifeCycle):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8607)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, ACTIVE_SENDMESSAGE, 0, 0, 0)
    cl_action.CommonChangeMoveDis(oWarrior, oLifeCycle, '15201SuitRecord', 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    if cl_condition.CheckIsAIHero(oWarrior, oLifeCycle):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 4000, 0, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8607)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, ACTIVE_SENDMESSAGE, 0, 0, 0)
    cl_action.CommonChangeMoveDis(oWarrior, oLifeCycle, '15201SuitRecord', 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    if cl_condition.CheckIsAIHero(oWarrior, oLifeCycle):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 5000, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8607, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33504, 200, { }, 0, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, (lambda *a: 800 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 20, 20, 3)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, (lambda *a: 800 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
        'Cnt': 2,
        'ElementExceptionRatio': 3000,
        'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': '15201SuitRecord' }))) >= 25:
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0, 0)
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
            'Cnt': 2,
            'ElementExceptionRatio': 3000,
            'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, (lambda *a: 700 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 20, 20, 6)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, (lambda *a: 700 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
        'Cnt': 2,
        'ElementExceptionRatio': (lambda *a: 3000 + (Func728(*a, **{
'sAttr': 'MoveSpeed' }) // 100) * 1500),
        'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': '15201SuitRecord' }))) >= 20:
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0, 0)
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
            'Cnt': 2,
            'ElementExceptionRatio': (lambda *a: 3000 + (Func728(*a, **{
'sAttr': 'MoveSpeed' }) // 100) * 1500),
            'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 8, 1, (lambda *a: 600 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 20, 20, 9)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 8, 1, (lambda *a: 600 / (10000 + Func744(*a, **{
'iType': 2 })) / 10000), 0, 1, { })
    cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
        'Cnt': 3,
        'ElementExceptionRatio': (lambda *a: 3000 + (Func728(*a, **{
'sAttr': 'MoveSpeed' }) // 100) * 1500),
        'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': '15201SuitRecord' }))) >= 20:
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, '15201SuitRecord', OBJECT_OWNER, 0, 0)
        cl_action.CommonTriggerSeasonSuitPerformShow(oWarrior, oEventCB.GetCBLifeCycle(), 15124)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 8607, 0, {
            'Cnt': 3,
            'ElementExceptionRatio': (lambda *a: 3000 + (Func728(*a, **{
'sAttr': 'MoveSpeed' }) // 100) * 1500),
            'Att': (lambda *a: 50000 + Func223(*a) * 12500) })


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8607, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AIDamage', (lambda *a: Func587(*a) * 0.3))
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 15201,
'sArgs': 'AIDamage' })), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, 0, None, None)
        cl_evact.EventTriggerTargetEleAbnormal(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 15201,
'sArgs': 'AIDamage' })))


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8607, 1, 0):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 15201
    m_Name = '迅捷流星'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11 }
    m_BaseArgData = { }
    m_DieDisable = 0

