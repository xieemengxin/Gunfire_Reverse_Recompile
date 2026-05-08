# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4212.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4212.pyc
# Source Generated with Decompyle++
# File: p4212.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32460, 0, { }, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeMinorPerformEnergyCost(oWarrior, oEventCB, 6000)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1418, 0, None):
        if oWarrior.Energy() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyCost' }))):
            if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
                cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                    5: 7000 }, None)
            else:
                cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)
        elif cl_evcon.CheckHasState(oWarrior, oEventCB, 32460):
            if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
                cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                    5: 7000 }, None)
            else:
                cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)
        else:
            cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1418)


def DoCallBackAction2(oEventCB, oWarrior):
    if oWarrior.Energy() >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyCost' }))):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                5: 7000 }, None)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)
    elif cl_evcon.CheckHasState(oWarrior, oEventCB, 32460):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                5: 7000 }, None)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)
    else:
        cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1418)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32460):
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                5: 7000 }, None)
        else:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)
    else:
        cl_action.CommonHaltPointPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1418)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2809) == 3:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            5: 7000 }, None)
    else:
        cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evact.EventGetTMinorPerformEnergyCost(oWarrior, oEventCB), None)


class CPerform(CCustomPerform):
    m_SID = 4212
    m_Name = '妖星被动'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

