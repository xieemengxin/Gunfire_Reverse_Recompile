# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51645.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51645.pyc
# Source Generated with Decompyle++
# File: p51645.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import INKVALUE_SUB, OBJ_SELF
from cl_newformula import Func717, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 60)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 60)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddRatio', 250)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DuringTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxExtraAddRatio', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 120)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'EnergyCost') > 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyNum', cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'EnergyCost') // 100)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 39700, 1, 0, 0, 0):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
                'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' })),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'EnergyNum' })), 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') < 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyNum', -cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange'))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 39700, 1, 0, 0, 0):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
                'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' })),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'EnergyNum' })), 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 39700, 1, 0, 0, 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
            'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' }) + min(int((Func839(*a) // 3) * Func717(*a, **{
'sArg': 'ExtraAddRatio' })), int(Func717(*a, **{
'sArg': 'MaxExtraAddRatio' })))),
            'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1, 1, 0)
    cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'EnergyNum' })), 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'EnergyCost') > 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyNum', cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'EnergyCost') // 100)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 39700, 1, 0, 0, 0):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
                'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' }) + min(int((Func839(*a) // 3) * Func717(*a, **{
'sArg': 'ExtraAddRatio' })), int(Func717(*a, **{
'sArg': 'MaxExtraAddRatio' })))),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'EnergyNum' })), 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })))


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') < 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyNum', -cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange'))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 39700, 1, 0, 0, 0):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })), {
                'AddRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddRatio' }) + min(int((Func839(*a) // 3) * Func717(*a, **{
'sArg': 'ExtraAddRatio' })), int(Func717(*a, **{
'sArg': 'MaxExtraAddRatio' })))),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1, 1, 0)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39700, (lambda *a: Func717(*a, **{
'sArg': 'EnergyNum' })), 0, 1, (lambda *a: Func717(*a, **{
'sArg': 'DuringTime' })))


class CPerform(CCustomPerform):
    m_SID = 51645
    m_Name = '资源转换'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

