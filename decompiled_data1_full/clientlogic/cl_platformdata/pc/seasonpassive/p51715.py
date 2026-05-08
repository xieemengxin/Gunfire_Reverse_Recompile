# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51715.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51715.pyc
# Source Generated with Decompyle++
# File: p51715.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_S8THIRDACTIVE
from cl_newformula import Func336, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39759):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39759, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39759):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39759, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    if cl_condition.HasState(oWarrior, oLifeCycle, 39759):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39759, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39759, 'EnableCount', 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'ThirdActiveCost', 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: Func336(*a, **{
'sKey': 'ThirdActiveCost' })))
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'CountEnergy' }))) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CostEnergy') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'CountEnergy' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'CostEnergy' }) // Func859(*a, **{
'sAttr': 'CountEnergy' })))
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CostEnergy', (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'CountEnergy' })))
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39759, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'AddCountMul' })), 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if not cl_condition.CommonCheckStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 39759, 'EnableCount', 0, 0):
        cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 39759)


class CPerform(CCustomPerform):
    m_SID = 51715
    m_Name = '暴击'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'CountEnergy': 10,
            'AddCountMul': 2 },
        2: {
            'CountEnergy': 10,
            'AddCountMul': 4 },
        3: {
            'CountEnergy': 10,
            'AddCountMul': 8 } }

