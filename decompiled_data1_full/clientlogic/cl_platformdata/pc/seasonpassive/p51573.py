# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51573.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51573.pyc
# Source Generated with Decompyle++
# File: p51573.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717, Func851
from cl_commondefines import S7_MODULE_POINT_CHANGE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 1000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39729, 0, {
        'AbnormalSourceDam': (lambda *a: Func717(*a, **{
'sArg': 'AbnormalSourceDam' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 2000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39729, 0, {
        'AbnormalSourceDam': (lambda *a: Func717(*a, **{
'sArg': 'AbnormalSourceDam' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AbnormalSourceDam', 3000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39729, 0, {
        'AbnormalSourceDam': (lambda *a: Func717(*a, **{
'sArg': 'AbnormalSourceDam' })),
        'ExtraSourceDam': 100 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39726, 'ExtraSourceDam', 100, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 3, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39726, 'ExtraSourceDam', 1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 39726):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39726, 0, {
            'AbnormalSourceDam': 0 }, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 39726, 'AbnormalSourceDam', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AbnormalSourceDam'))
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39726, -1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBAddStateArgVal(oWarrior, oEventCB, 39726, 'AbnormalSourceDam', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AbnormalSourceDam'))
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39726, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39729, (lambda *a: Func851(*a, **{
'dCheckModuleTag': { },
'iExcludeOverflow': 1 }) // 3), 1)


class CPerform(CCustomPerform):
    m_SID = 51573
    m_Name = '#NT#元素专精'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

