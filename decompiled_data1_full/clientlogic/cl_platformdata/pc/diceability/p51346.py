# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51346.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51346.pyc
# Source Generated with Decompyle++
# File: p51346.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import COST_BAGBULLET_WEAPON, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, PF_SUBMSG_CLIENTACTIVE
from cl_newformula import Func208, Func215, Func651, Func717

def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostMax', 40)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4502', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4503', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4504', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 25)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12035)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 0, 0, {
        'GainEffect': 25 }, 1)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 12035)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostMax', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4502', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4503', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4504', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 50)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12035)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 0, 0, {
        'GainEffect': 50 }, 1)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 12035)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CostMax', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4502', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4503', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt4504', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 100)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12035)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 0, 0, {
        'GainEffect': 100 }, -1)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 12035)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func208(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostNum', (lambda *a: Func208(*a)))
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SID' })), {
            4502: 5,
            4503: 6,
            4504: 7 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func215(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CostNum', (lambda *a: Func215(*a)))
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SID' })), {
            4502: 5,
            4503: 6,
            4504: 7 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SID' })), {
        4502: 5,
        4503: 6,
        4504: 7 })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurNum') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostMax'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TriggerCnt', (lambda *a: min(5, int(Func717(*a, **{
'sArg': 'CurNum' }) // Func717(*a, **{
'sArg': 'CostMax' })))))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurNum', (lambda *a: -Func717(*a, **{
'sArg': 'TriggerCnt' }) * Func717(*a, **{
'sArg': 'CostMax' })))
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 9, (lambda *a: Func717(*a, **{
'sArg': 'TriggerCnt' })))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurNum', (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'Cnt4502' })))


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurNum', (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'Cnt4503' })))


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurNum', (lambda *a: Func717(*a, **{
'sArg': 'CostNum' }) * Func717(*a, **{
'sArg': 'Cnt4504' })))


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12035, 0, 0):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func717(*a, **{
'sArg': 'AddLuckyHit' })), 0)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12035, '', 0, 1, {
        'AddLuckyHit': (lambda *a: Func717(*a, **{
'sArg': 'AddLuckyHit' })) })


class CPerform(CCustomPerform):
    m_SID = 51346
    m_Name = '充能打击'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

