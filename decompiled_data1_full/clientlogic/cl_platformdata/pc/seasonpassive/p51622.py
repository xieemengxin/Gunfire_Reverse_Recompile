# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51622.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51622.pyc
# Source Generated with Decompyle++
# File: p51622.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 4000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 6000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39683, 0, {
        'AddSpeed': 200 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 8000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39683, 0, {
        'AddSpeed': 400 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 10000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39683, 0, {
        'AddSpeed': 600 }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'DamInterval', (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' })), 0, 0)
    else:
        cl_action.CommonChangeThrowPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' })), 0, 0)
    cl_action.CommonChangeThrowPerformUse(oWarrior, oEventCB.GetCBLifeCycle(), 3, 0)


class CPerform(CCustomPerform):
    m_SID = 51622
    m_Name = '次要消耗'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

