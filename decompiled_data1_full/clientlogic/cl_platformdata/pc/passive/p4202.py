# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4202.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4202.pyc
# Source Generated with Decompyle++
# File: p4202.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func235

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7974, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 3, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HP_RADIO_SUB, 1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 0, -1000, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 85, 0, None, None)
    cl_action.CommonSetMaxCustomData(oWarrior, oLifeCycle, 'PhaseRatio', 80)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1001) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1003):
        cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
            39202: 50 })
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1002):
            cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
            cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
                39201: 100 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetPhase(oWarrior, oEventCB, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if (cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1001) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1003) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1002)) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39205, 1, None):
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 7974, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 7974, None, None) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 5 - Func235(*a, **{
'sType': 'RidingAlone' }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1001) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1003):
            cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
            cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
                39202: 50 })
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            if cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1002):
                cl_evact.EventCBNonLockEnemyTarget(oWarrior, oEventCB)
                cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
                    39201: 100 })
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 7974, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if (cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1001) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1003) or cl_evcon.CheckCurrentPFAI(oWarrior, oEventCB, 1002)) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39205, 1, None):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 7974, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 4202
    m_Name = '章鱼-阶段1'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

