# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51629.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51629.pyc
# Source Generated with Decompyle++
# File: p51629.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717, Func746, Func839
from cl_commondefines import S7_MODULE_POINT_CHANGE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDebuffProb', 500)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39689, 0, {
        'AddDebuffProb': (lambda *a: Func717(*a, **{
'sArg': 'AddDebuffProb' }) // 100) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDebuffProb', 1000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39689, 0, {
        'AddDebuffProb': (lambda *a: Func717(*a, **{
'sArg': 'AddDebuffProb' }) // 100) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDebuffProb', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddDebuffProb', 100)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39689, 0, {
        'AddDebuffProb': (lambda *a: Func717(*a, **{
'sArg': 'AddDebuffProb' }) // 100),
        'ExtraAddDebuffProb': (lambda *a: Func717(*a, **{
'sArg': 'ExtraAddDebuffProb' }) // 100) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'DebuffFactor', 0, (lambda *a: Func717(*a, **{
'sArg': 'AddDebuffProb' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39689, (lambda *a: Func839(*a) // 3), 1)
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'DebuffFactor', 0, (lambda *a: Func717(*a, **{
'sArg': 'AddDebuffProb' }) + Func746(*a, **{
'iStateSID': 39689 }) * Func717(*a, **{
'sArg': 'ExtraAddDebuffProb' })))


class CPerform(CCustomPerform):
    m_SID = 51629
    m_Name = '元素异常'
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

