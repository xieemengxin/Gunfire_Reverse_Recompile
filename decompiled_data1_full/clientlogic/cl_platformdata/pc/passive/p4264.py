# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4264.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4264.pyc
# Source Generated with Decompyle++
# File: p4264.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_USE_SHIELD, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, STATE_EFF_SUBSPD
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Toughness', 0, 100, 1)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonIgnoreStateEffectAdd(oWarrior, oLifeCycle, STATE_EFF_SUBSPD, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 1)
    cl_action.CommonChangeEnergy(oWarrior, oLifeCycle, 30000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 1009, 0)
    if oWarrior.m_SID == 39251:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Shield() > 0:
        cl_evact.EventCBConvertPredictDamToPoinType(oWarrior, oEventCB, DAM_USE_SHIELD)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8136) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8136, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8136, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8137) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8137, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8137, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8138) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8138, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8138, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CheckWarCycle(oWarrior, oEventCB.GetCBLifeCycle()) >= 10:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8136) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8136, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8136, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8137) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8137, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8137, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8138) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8138, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8138, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
        elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if None.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4250,
'sArgs': 'pf_4250' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4250, 'pf_4250', 1, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.CheckWarCycle(oWarrior, oEventCB.GetCBLifeCycle()) >= 10:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8136) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8136, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8136, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8137) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8137, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8137, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8138) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8138, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8138, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
        elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7997) == 0:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7997, 0, { }, 1)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7997, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
            cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
    if None.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7998) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7998, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7998, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 7999) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 7999, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7999, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 8000) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 8000, 0, { }, 1)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 8000, (lambda *a: Func361(*a, **{
'sid': 4303,
'sArgs': 'pf_4303' })))
        cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 4303, 'pf_4303', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 4264
    m_Name = '妖王-阶段6'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

