# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3215.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3215.pyc
# Source Generated with Decompyle++
# File: p3215.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func560, Func563, Func651
from cl_commondefines import QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, STATE_COUNT_MAX

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 0, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddAtt', 1000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateCountMax', 6, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateTime', 600, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 2, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddAtt', 1000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddLuckyHit', 10, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateCountMax', 6, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateTime', 700, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, -1, 3, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddAtt', 1500, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddLuckyHit', 15, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'AddCrazyEff', 3000, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateCountMax', 8, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3215, 'StateTime', 800, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Empty' }))) == 1:
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32754):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32754, (lambda *a: Func563(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32754):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
            'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
        cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32754, (lambda *a: Func563(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Empty' }))) == 1:
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32754):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32754, (lambda *a: Func563(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Empty' }))) == 1 or cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'ClearAll'):
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Quality' })), {
            QUALITY_TYPE_CURSE: 7,
            QUALITY_TYPE_HIGH: 5,
            QUALITY_TYPE_NORMAL: 5,
            QUALITY_TYPE_LOW: 4 })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Empty' }))) == 1:
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32754):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32754, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32754, (lambda *a: Func563(*a)), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Empty' }))) == 1 or cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'ClearAll'):
        cl_evact.EventCBDirectEventCBFuncByNum(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Quality' })), {
            QUALITY_TYPE_CURSE: 8,
            QUALITY_TYPE_HIGH: 6,
            QUALITY_TYPE_NORMAL: 5,
            QUALITY_TYPE_LOW: 4 })


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32892):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32892, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
            'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
        cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32892, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32892, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))


def DoCallBackAction5(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32893):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32893, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
            'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLuckyHit') }, 1, 0, 0)
        cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32893, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32893, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))


def DoCallBackAction6(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32894):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
            'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCrazyEff') }, 1, 0, 0)
        cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32894, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        4: 5000,
        5: 5000 }, 1)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func560(*a))):
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32892):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32892, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddAtt') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32892, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32892, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32893):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32893, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddLuckyHit') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32893, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32893, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32894):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'), {
                'GainEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCrazyEff') }, 1, 0, 0)
            cl_action.CommonChangeStateAttr(oWarrior, oEventCB.GetCBLifeCycle(), 32894, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCountMax'), STATE_COUNT_MAX, None)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32894, 1, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateTime'))
    else:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            4: 3333,
            5: 3333,
            6: 3334 }, 1)


class CPerform(CCustomPerform):
    m_SID = 3215
    m_Name = '全力一押'
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
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 113

