# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51658.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51658.pyc
# Source Generated with Decompyle++
# File: p51658.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 4500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.CommonChangeThrowPerformExtraUse(oWarrior, oLifeCycle, 2, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 9000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.CommonChangeThrowPerformExtraUse(oWarrior, oLifeCycle, 2, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 13500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerAddRatio', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxExtraAddRatio', 7500)
    cl_action.CommonChangeThrowPerformExtraUse(oWarrior, oLifeCycle, 2, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39714, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
            'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' })) }, 1, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39714, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
            'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' }) + min(int(Func717(*a, **{
'sArg': 'PerAddRatio' }) * Func839(*a) // 1), int(Func717(*a, **{
'sArg': 'MaxExtraAddRatio' })))) }, 1, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 51658
    m_Name = '激活器'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

