# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51588.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51588.pyc
# Source Generated with Decompyle++
# File: p51588.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_formula
from cl_platformdata.custom.seasonpassive.customaction import CustomAction51588_1 as CustomAction
from cl_platformdata.custom.seasonpassive.customaction import CustomAction51588_2 as CustomAction2
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func208, Func215, Func332, Func410, Func651, Func717
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COST_BAGBULLET_WEAPON, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1992)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv1CostCount' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33951, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv1CountDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TalentDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv1TalentDam' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 12, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 12, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992CountDam', (lambda *a: Func717(*a, **{
'sArg': 'CountDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 100)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1992)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv2CostCount' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33951, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv2CountDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TalentDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv2TalentDam' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 12, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 12, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992CountDam', (lambda *a: Func717(*a, **{
'sArg': 'CountDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 100)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1992)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv3CostCount' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33951, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv3CountDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TalentDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv3TalentDam' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 12, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 12, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992CountDam', (lambda *a: Func717(*a, **{
'sArg': 'CountDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 100)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33941, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 7, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NeedCreateDamCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv4NeedCreateDamCount' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv4AddSummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxSummon', (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxSummon' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv4SummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxSummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxSummonTime' })))
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'MaxSumminTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxSummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv4CostCount' })))
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1992)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33951, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv4CountDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TalentDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv4TalentDam' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 12, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 12, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992CountDam', (lambda *a: Func717(*a, **{
'sArg': 'CountDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 100)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33941, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 7, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NeedCreateDamCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv5NeedCreateDamCount' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddSummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv5AddSummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxSummon', (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxSummon' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv5SummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxSummonTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxSummonTime' })))
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'MaxSumminTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxSummonTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostCount', (lambda *a: Func717(*a, **{
'sArg': 'Lv5CostCount' })))
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1992)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33951, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv5CountDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TalentDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv5TalentDam' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 12, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 12, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992CountDam', (lambda *a: Func717(*a, **{
'sArg': 'CountDam' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 100)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func208(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostNum', (lambda *a: Func208(*a)))
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SID' })), {
            4502: 2,
            4503: 3,
            4504: 4 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func215(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostNum', (lambda *a: Func215(*a)))
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SID' })), {
            4502: 2,
            4503: 3,
            4504: 4 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33951, (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'STD_AddCount' })), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33951, (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'BIG_AddCount' })), 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33951, (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'CUSTOM_AddCount' })), 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33951) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CostCount'):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func410(*a, **{
'sid': 33951 }) // Func717(*a, **{
'sArg': 'CostCount' })))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33951, (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * Func717(*a, **{
'sArg': 'CostCount' })), 0)
        CustomAction2(oWarrior, oEventCB, {
            'AddTime': 500,
            'AddCount': (lambda *a: Func717(*a, **{
'sArg': 'AddCount' })) })


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'pfid' }))) == 51588:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SummonNum', 1)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'pfid' }))) == 51588:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SummonNum', -1)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1992, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CreateDamCount', 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CreateDamCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NeedCreateDamCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CreateDamCount', 0)
            CustomAction(oWarrior, oEventCB, {
                'AddLifeTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSummonTime'),
                'MaxSummonTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxSummonTime') })
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33941, 0)
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SummonNum') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MaxSummon'):
                cl_evact.EventCBCreateSummon(oWarrior, oEventCB, 1085, (lambda *a: Func717(*a, **{
'sArg': 'SummonTime' })), cl_evact.EventCBGetTargetPos(oWarrior, oEventCB), 1, 1)
            else:
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33941, 1, 0)


def DoCallBackAction9(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CreateDamCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NeedCreateDamCount'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CreateDamCount', 0)
        CustomAction(oWarrior, oEventCB, {
            'AddLifeTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSummonTime'),
            'MaxSummonTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxSummonTime') })
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33941, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SummonNum') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MaxSummon'):
            cl_evact.EventCBCreateSummon(oWarrior, oEventCB, 1085, (lambda *a: Func717(*a, **{
'sArg': 'SummonTime' })), cl_evact.EventCBGetTargetPos(oWarrior, oEventCB), 1, 1)
        else:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33941, 1, 0)


def DoCallBackAction10(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SummonNum') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MaxSummon'):
        cl_evact.EventCBCreateSummon(oWarrior, oEventCB, 1085, (lambda *a: Func717(*a, **{
'sArg': 'SummonTime' })), cl_evact.EventCBGetTargetPos(oWarrior, oEventCB), 1, 1)


def DoCallBackAction11(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1992, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CreateDamCount', 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CreateDamCount') >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NeedCreateDamCount'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CreateDamCount', 0)
            CustomAction(oWarrior, oEventCB, {
                'AddLifeTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddSummonTime'),
                'MaxSummonTime': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxSummonTime') })
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33941, 0)
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('SummonNum') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('MaxSummon'):
                cl_evact.EventCBCreateSummon(oWarrior, oEventCB, 1085, (lambda *a: Func717(*a, **{
'sArg': 'SummonTime' })), cl_evact.EventCBGetTargetPos(oWarrior, oEventCB), 1, 1)
            else:
                cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33941, 1, 0)


def DoCallBackAction12(oEventCB, oWarrior):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oEventCB.GetCBLifeCycle(), 'PF1992TalentDam', (lambda *a: Func332(*a) * Func717(*a, **{
'sArg': 'TalentDam' })))


class CPerform(CCustomPerform):
    m_SID = 51588
    m_Name = '#NT#毒雾'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11,
        12: DoCallBackAction12 }
    m_BaseArgData = {
        'Lv4NeedCreateDamCount': 15,
        'Lv4AddSummonTime': 500,
        'Lv4MaxSummon': 2,
        'Lv4SummonTime': 1000,
        'Lv5DamHit': 12,
        'Lv5NeedCreateDamCount': 15,
        'Lv5AddSummonTime': 500,
        'Lv5MaxSummon': 2,
        'Lv5SummonTime': 1000,
        'Lv4MaxSummonTime': 3000,
        'Lv5MaxSummonTime': 3000,
        'Lv1CostCount': 15,
        'Lv2CostCount': 15,
        'Lv3CostCount': 15,
        'Lv4CostCount': 10,
        'Lv5CostCount': 10,
        'STD_AddCount': 1,
        'BIG_AddCount': 5,
        'CUSTOM_AddCount': 15,
        'Lv1CountDam': 10000,
        'Lv2CountDam': 15000,
        'Lv3CountDam': 20000,
        'Lv4CountDam': 25000,
        'Lv5CountDam': 30000,
        'Lv1TalentDam': 100,
        'Lv2TalentDam': 200,
        'Lv3TalentDam': 400,
        'Lv4TalentDam': 600,
        'Lv5TalentDam': 1000 }
    m_DieDisable = 0

