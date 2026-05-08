# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51653.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51653.pyc
# Source Generated with Decompyle++
# File: p51653.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func343, Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 1200, 1200, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 900, 900, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 600, 600, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func602(*a) * 3)) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10)):
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 2, 0)
    else:
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func602(*a) * 5)) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }) * 10)):
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 2, 0)
    else:
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51653
    m_Name = 'Q回复'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

