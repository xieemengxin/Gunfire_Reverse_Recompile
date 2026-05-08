# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51642.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51642.pyc
# Source Generated with Decompyle++
# File: p51642.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StatusEffect', 500)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39704, (lambda *a: -Func717(*a, **{
'sArg': 'StatusEffect' })), 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StatusEffect', 1000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39704, (lambda *a: -Func717(*a, **{
'sArg': 'StatusEffect' })), 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StatusEffect', (lambda *a: 1500 + min(750, Func839(*a) * 50)))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, -1, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39704, (lambda *a: -Func717(*a, **{
'sArg': 'StatusEffect' })), 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 39704):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39704, 0, { }, 0, 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39704, (lambda *a: Func717(*a, **{
'sArg': 'StatusEffect' })), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39704, (lambda *a: -Func717(*a, **{
'sArg': 'StatusEffect' })), 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'StatusEffect', (lambda *a: 1500 + min(750, Func839(*a) * 50)))
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 39704):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39704, 0, { }, 0, 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39704, (lambda *a: Func717(*a, **{
'sArg': 'StatusEffect' })), 0)


class CPerform(CCustomPerform):
    m_SID = 51642
    m_Name = '加速冷却'
    m_MaxLevel = 3
    m_MaxStack = 3
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

