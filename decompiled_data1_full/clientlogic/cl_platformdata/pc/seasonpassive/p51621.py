# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51621.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51621.pyc
# Source Generated with Decompyle++
# File: p51621.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import INKVALUE_SUB, OBJECT_OWNER
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 0.2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddRatio', 6)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, min(int(max(((cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange') - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_OWNER)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') < 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, min(int(max(((-cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') * 100 - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')):
        cl_action.CommonModifyInkValue(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange'), '', {
            'Fixed': 1 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 1000, (lambda *a: (min(int(max(((cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange') - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio') + min(int(Func717(*a, **{
'sArg': 'MaxAddRatio' })), int(Func839(*a) * Func717(*a, **{
'sArg': 'AddRatio' })))) * 10)):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_OWNER)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange'))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') < 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 1000, (lambda *a: (min(int(max(((-cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') * 100 - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio') + min(int(Func717(*a, **{
'sArg': 'MaxAddRatio' })), int(Func839(*a) * Func717(*a, **{
'sArg': 'AddRatio' })))) * 10)):
        cl_action.CommonModifyInkValue(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange'), '', {
            'Fixed': 1 })


class CPerform(CCustomPerform):
    m_SID = 51621
    m_Name = 'E-内力流转'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

