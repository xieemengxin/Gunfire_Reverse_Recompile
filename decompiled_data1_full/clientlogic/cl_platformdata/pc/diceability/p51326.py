# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51326.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51326.pyc
# Source Generated with Decompyle++
# File: p51326.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE, DUAL_STATE_BEGIN, DUAL_STATE_END

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAdd', 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAdd', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddRatio', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAddMax', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAdd', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddRatio', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAddMax', 40)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseAdd', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddRatio', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtAddMax', 80)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_BaseAdd', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseAdd'))
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_ExtraAddRatio', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraAddRatio'))
    cl_action.CommonAddCustomIntData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51326_EnableNum', 1, 1)
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_ExtAddMax', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtAddMax'))
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33683):
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, {
            'StateSID': 33683 })
    else:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33683, 0, { }, 0)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201):
        if not cl_condition.CheckDualSate(oWarrior, oEventCB.GetCBLifeCycle()) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33684):
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33684, 0, { }, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 3, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 33684):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33684, 0, { }, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 33684):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33684, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonAddCustomIntData(oWarrior, oEventCB.GetCBLifeCycle(), 'p51326_EnableNum', -1, 1)
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_BaseAdd', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseAdd'))
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_ExtraAddRatio', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraAddRatio'))
    cl_evact.EventCBAddCustomData(oWarrior, oEventCB, 'p51326_ExtAddMax', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtAddMax'))
    if cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'p51326_EnableNum'):
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, {
            'StateSID': 33683 })
    else:
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33683, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33684, 0)


class CPerform(CCustomPerform):
    m_SID = 51326
    m_Name = '武器等级'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

