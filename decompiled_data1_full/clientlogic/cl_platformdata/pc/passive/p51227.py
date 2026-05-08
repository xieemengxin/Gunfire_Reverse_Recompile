# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51227.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51227.pyc
# Source Generated with Decompyle++
# File: p51227.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetStateArgVal(oWarrior, oEventCB, 33964, 'st33964Num', 3)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetStateArgVal(oWarrior, oEventCB, 33964, 'st33964Num', 2)


class CPerform(CCustomPerform):
    m_SID = 51227
    m_Name = 'S7房间挑战3额外被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

