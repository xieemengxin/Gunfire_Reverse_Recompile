# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5347.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5347.pyc
# Source Generated with Decompyle++
# File: p5347.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_ADD, ARMOR_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 0, ARMOR_RADIO_SUB, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 1, ARMOR_RADIO_ADD, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 5347
    m_Name = '#NT#冲锋兵转阶段'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

