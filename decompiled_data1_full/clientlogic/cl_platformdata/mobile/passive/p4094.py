# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4094.pyc
# Source Generated with Decompyle++
# File: p4094.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB
from cl_newformula import Func341

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8031, 1000, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7072, 0, { }, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 25, HP_RADIO_SUB, 0)
    cl_action.CommonTriggerCG(oWarrior.m_Game, 64, 1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 62, 0, None, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, (lambda *a: Func341(*a) + 1))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 0, 1, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1009, 1100, { }, 1, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7101, 1000, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4094
    m_Name = '三幕Boss阶段5'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

