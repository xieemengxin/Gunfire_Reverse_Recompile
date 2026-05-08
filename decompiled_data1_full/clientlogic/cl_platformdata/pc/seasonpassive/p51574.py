# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51574.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51574.pyc
# Source Generated with Decompyle++
# File: p51574.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func332, Func340, Func717, Func804

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12041)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 60000 + Func332(*a) * 10000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedTimes', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12041)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 90000 + Func332(*a) * 20000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedTimes', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12041)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 120000 + Func332(*a) * 30000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedTimes', 300)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12041)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 150000 + Func332(*a) * 40000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedTimes', 300)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12041)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Att', (lambda *a: 180000 + Func332(*a) * 50000))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpeedTimes', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerDis', 10)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'p51574', 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'p51574',
'iAddExtInfo': 1 }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerDis' }))):
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 1, (lambda *a: min(Func340(*a, **{
'sKey': 'p51574',
'iAddExtInfo': 1 }) // Func717(*a, **{
'sArg': 'TriggerDis' }), 5)), None)
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51574', 0, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12041, '', 0, 1, {
        'Att': (lambda *a: Func717(*a, **{
'sArg': 'Att' })),
        'AttCnt': (lambda *a: Func717(*a, **{
'sArg': 'AttCnt' })),
        'SpeedTimes': (lambda *a: Func717(*a, **{
'sArg': 'SpeedTimes' })) })
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
        'pfid': 51574,
        'Item': (lambda *a: Func804(*a)),
        'TriggerPerformID': 12041 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51574', 0, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 51574
    m_Name = '#NT#弹射骰子'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = {
        'TriggerDis': 15 }
    m_DieDisable = 0

