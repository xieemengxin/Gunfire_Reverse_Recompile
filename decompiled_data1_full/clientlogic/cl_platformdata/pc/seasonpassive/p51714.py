# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51714.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51714.pyc
# Source Generated with Decompyle++
# File: p51714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_S8THIRDACTIVE
from cl_newformula import Func336, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerCostEnergy', 40)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerCostEnergy', 20)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CDReduce', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PerCostEnergy', 10)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalCostEnergy', (lambda *a: Func336(*a, **{
'sKey': 'ThirdActiveCost' })))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TotalCostEnergy') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PerCostEnergy'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EffectCount', (lambda *a: Func717(*a, **{
'sArg': 'TotalCostEnergy' }) // Func717(*a, **{
'sArg': 'PerCostEnergy' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TotalCostEnergy', (lambda *a: -Func717(*a, **{
'sArg': 'EffectCount' }) * Func717(*a, **{
'sArg': 'PerCostEnergy' })))
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, (lambda *a: Func717(*a, **{
'sArg': 'EffectCount' }) * Func717(*a, **{
'sArg': 'CDReduce' })))


class CPerform(CCustomPerform):
    m_SID = 51714
    m_Name = '使用回复'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

