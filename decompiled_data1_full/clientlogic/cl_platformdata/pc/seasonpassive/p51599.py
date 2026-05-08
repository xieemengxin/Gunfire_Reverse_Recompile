# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51599.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51599.pyc
# Source Generated with Decompyle++
# File: p51599.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51599SetSpread', 100)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51599SetSpread', 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51599SetSpread', 300)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p51599SetSpread', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51599SetMaxCount', (lambda *a: Func308(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51599SetMaxCount', 0)


class CPerform(CCustomPerform):
    m_SID = 51599
    m_Name = '#NT#毒雾上限'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

