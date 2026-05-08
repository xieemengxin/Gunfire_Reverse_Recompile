# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51673.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51673.pyc
# Source Generated with Decompyle++
# File: p51673.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func558, Func859
from cl_commondefines import HPARMORSHIELD_RADIO_ADD, HPARMORSHIELD_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 80:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_ADD, 1)


def DisableAction1(oWarrior, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('PF51673_ColdTimeEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'ColdTimeRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 80:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_ADD, 1)


def DisableAction2(oWarrior, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('PF51673_ColdTimeEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'ColdTimeRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 80:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 60:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_ADD, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HPARMORSHIELD_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HPARMORSHIELD_RADIO_ADD, 3)


def DisableAction3(oWarrior, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('PF51673_ColdTimeEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'ColdTimeRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)
    if oLifeCycle.m_Owner.GetArgValue('PF51673_DamRatioEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'DamRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)


def Action4(oWarrior, oLifeCycle):
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 80:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func558(*a))) <= 60:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HPARMORSHIELD_RADIO_ADD, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HPARMORSHIELD_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, HPARMORSHIELD_RADIO_ADD, 3)


def DisableAction4(oWarrior, oLifeCycle):
    if oLifeCycle.m_Owner.GetArgValue('PF51673_ColdTimeEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'ColdTimeRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)
    if oLifeCycle.m_Owner.GetArgValue('PF51673_DamRatioEnable'):
        cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39757, 'DamRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39757, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 39757):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 0, { }, 0)
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF51673_ColdTimeEnable'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF51673_ColdTimeEnable', 1)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 'ColdTimeRatio', (lambda *a: Func859(*a, **{
'sAttr': 'ColdTimeRatio' })), 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF51673_ColdTimeEnable'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF51673_ColdTimeEnable', 0)
        cl_action.CommonRemoveStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 'ColdTimeRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39757, -1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF51673_DamRatioEnable'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF51673_DamRatioEnable', 1)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 'DamRatio', (lambda *a: Func859(*a, **{
'sAttr': 'DamRatio' })), 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF51673_DamRatioEnable'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'PF51673_DamRatioEnable', 0)
        cl_action.CommonRemoveStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39757, 'DamRatio', 0, 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39757, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51673
    m_Name = '主要技能-刀尖舞者'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'ColdTimeRatio': 800 },
        2: {
            'ColdTimeRatio': 1600 },
        3: {
            'ColdTimeRatio': 2400,
            'DamRatio': 6000 },
        4: {
            'ColdTimeRatio': 3200,
            'DamRatio': 12000 } }

