# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4365.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4365.pyc
# Source Generated with Decompyle++
# File: p4365.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 5000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8087, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7023, 2000, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8113, 0, { }, 1)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 39028, 0, { })


class CPerform(CCustomPerform):
    m_SID = 4365
    m_Name = '【诡谲雪山】罗睺-阶段3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

