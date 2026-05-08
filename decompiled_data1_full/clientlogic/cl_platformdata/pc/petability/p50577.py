# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petability/p50577.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petability/p50577.pyc
# Source Generated with Decompyle++
# File: p50577.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.petability import CPetAbility as CCustomPerform
from cl_commondefines import PET_ABILITY_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (0, None, ((646,), (lambda a0: a0)))) < 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'pf_50577', (0, None, ((646,), (lambda a0: -a0))))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'pf_50577') >= 2000:
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33189, -1, 1, -1):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33189, (0, None, ((361, 50577, 'pf_50577'), (lambda a0: a0 // 2000))), 1, -1, 500)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33189, 0, { }, 1, 0)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33189, (0, None, ((361, 50577, 'pf_50577'), (lambda a0: a0 // 2000))), 1, -1, 500)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_50577', (0, None, ((3, ((361, 50577, 'pf_50577'), (lambda a0: a0)), 2000), (lambda a0: a0))))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33189, -1, 1, -1):
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33189, (0, None, ((361, 50577, 'pf_50577'), (lambda a0: a0 // 2000))), 1, -1, 500)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33189, 0, { }, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33189, (0, None, ((361, 50577, 'pf_50577'), (lambda a0: a0 // 2000))), 1, -1, 500)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'pf_50577', (0, None, ((3, ((361, 50577, 'pf_50577'), (lambda a0: a0)), 2000), (lambda a0: a0))))


class CPerform(CCustomPerform):
    m_SID = 50577
    m_Name = ''
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
    m_NeedLockTarget = 0
    m_Quality = PET_ABILITY_LOW
    m_LimitPet = ()
    m_ExcludePet = ()
    m_Weight = 0
    m_SpellPower = 0
    m_AutoCDCallBack = 0
    m_PetAttr = { }

