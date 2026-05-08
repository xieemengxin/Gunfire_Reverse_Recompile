# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51718.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51718.pyc
# Source Generated with Decompyle++
# File: p51718.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S8THIRDACTIVE_ENERGY_CHANGE_ADD
from cl_newformula import Func537, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39769):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39769, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39769):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39769, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39769):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39769, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39769, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AddEnergy', (lambda *a: Func537(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'EnergyRecovery' }))) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddEnergy') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'EnergyRecovery' }))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'AddEnergy' }) // Func859(*a, **{
'sAttr': 'EnergyRecovery' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AddEnergy', (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'EnergyRecovery' })))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39769, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'AddCountMul' })), 700)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_condition.CommonCheckStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39768, 'EnableCount', 0, 0):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 39769)


class CPerform(CCustomPerform):
    m_SID = 51718
    m_Name = '护盾/护甲上限'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'EnergyRecovery': 3,
            'AddCountMul': 1 },
        2: {
            'EnergyRecovery': 1,
            'AddCountMul': 1 },
        3: {
            'EnergyRecovery': 1,
            'AddCountMul': 3 } }

