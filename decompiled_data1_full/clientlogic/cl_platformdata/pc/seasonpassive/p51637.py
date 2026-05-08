# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51637.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51637.pyc
# Source Generated with Decompyle++
# File: p51637.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func340, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39694, 0, { }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 39694, 9, 0, 1, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerAdd', 3)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39694, 0, { }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 39694, 18, 0, 1, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerAdd', 6)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39694, 0, { }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 39694, 27, 0, 1, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerAdd', 9)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39694, 0, { }, 1)
    cl_action.CommonChangeStateMaxCount(oWarrior, oLifeCycle, 39694, 45, 0, 1, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerAdd', 9)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 50, 50, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRecordMoveDis(oWarrior, oEventCB, 'p51637', 0, 1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'p51637',
'iAddExtInfo': 1 }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerDis' }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39694, (lambda *a: (Func340(*a, **{
'sKey': 'p51637',
'iAddExtInfo': 1 }) // Func717(*a, **{
'sArg': 'TriggerDis' })) * Func717(*a, **{
'sArg': 'PerAdd' })), 1, 1, None)
        cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'p51637', 0, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39694, (lambda *a: Func717(*a, **{
'sArg': 'PerAdd' })), 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 51637
    m_Name = '机动充能'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'TriggerDis': 5,
        'PerAdd': 0 }
    m_DieDisable = 0

