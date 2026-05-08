# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51660.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51660.pyc
# Source Generated with Decompyle++
# File: p51660.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func207, Func308, Func343, Func347, Func602, Func717
from cl_commondefines import CHANGEWARCASHSUBMSG_ADD, COST_BAGBULLET_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCash', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRate', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCash', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRate', 30)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCash', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDTime', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRate', 40)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'PF-51660Num') == 0:
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'PF-51660Num', (lambda *a: max(1, Func343(*a, **{
'sid': 4508 }) * 100 / Func347(*a, **{
'sid': 4508 }))))
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'PF-51660Num') < 30:
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostCash'):
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func717(*a, **{
'sArg': 'CostCash' })))
            cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func602(*a) * Func717(*a, **{
'sArg': 'BulletRate' }) + 99) // 100), 0)
            cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW)
            cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_ADD)
            cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CDTime'), 0, 1, { })
        else:
            cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_ADD, 1, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'PF-51660Num') == 0:
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'PF-51660Num', (lambda *a: max(1, Func343(*a, **{
'sid': 4508 }) * 100 / Func347(*a, **{
'sid': 4508 }))))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostCash'):
        cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func717(*a, **{
'sArg': 'CostCash' })))
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func602(*a) * Func717(*a, **{
'sArg': 'BulletRate' }) + 99) // 100), 0)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW)
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_ADD)
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CDTime'), 0, 1, { })
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_ADD, 1, 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 5, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CDTime'), 0, 1, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func308(*a)), {
        1: 6,
        2: 7,
        3: 8 })


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 1, 0, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 1, 0, 2)
    cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_THROW, 1, 0, 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51660
    m_Name = '等价交换'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0

