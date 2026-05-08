# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3805.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3805.pyc
# Source Generated with Decompyle++
# File: p3805.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func377, Func717, Func770
from cl_commondefines import CREATE_PLANT, CURE_TYPE_PERFORM, DAM_USE_ALL, DAM_USE_SHIELD, OBJECT_OWNER, OBJ_SELF, OBJ_VICTIM, SETPHASE_PLANT

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountTime', (lambda *a: Func717(*a, **{
'sArg': 'LV1CountTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', (lambda *a: Func717(*a, **{
'sArg': 'LV1AddShield' })))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33784, 0, {
        'CountTime': (lambda *a: Func717(*a, **{
'sArg': 'CountTime' })),
        'StatusEffect': (lambda *a: Func717(*a, **{
'sArg': 'LV1AddMax' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountTime', (lambda *a: Func717(*a, **{
'sArg': 'LV2CountTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', (lambda *a: Func717(*a, **{
'sArg': 'LV2AddShield' })))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33784, 0, {
        'CountTime': (lambda *a: Func717(*a, **{
'sArg': 'CountTime' })),
        'StatusEffect': (lambda *a: Func717(*a, **{
'sArg': 'LV2AddMax' })),
        'AddShield': 'LV2AddShield' }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, SETPHASE_PLANT, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv2PlantSneerTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv2PlantSneerCD' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerRange', (lambda *a: Func717(*a, **{
'sArg': 'Lv2PlantSneerRange' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv2TreeSneerTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv2TreeSneerCD' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerRange', (lambda *a: Func717(*a, **{
'sArg': 'Lv2TreeSneerRange' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountTime', (lambda *a: Func717(*a, **{
'sArg': 'LV3CountTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddShield', (lambda *a: Func717(*a, **{
'sArg': 'LV3AddShield' })))
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33784, 0, {
        'CountTime': (lambda *a: Func717(*a, **{
'sArg': 'CountTime' })),
        'StatusEffect': (lambda *a: Func717(*a, **{
'sArg': 'LV3AddMax' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, SETPHASE_PLANT, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv3PlantSneerTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv3PlantSneerCD' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PlantSneerRange', (lambda *a: Func717(*a, **{
'sArg': 'Lv3PlantSneerRange' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerTime', (lambda *a: Func717(*a, **{
'sArg': 'Lv3TreeSneerTime' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv3TreeSneerCD' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TreeSneerRange', (lambda *a: Func717(*a, **{
'sArg': 'Lv3TreeSneerRange' })))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func770(*a))) and cl_evcon.CheckDeadlyPredictDam(oWarrior, oEventCB, OBJECT_OWNER):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'LV3CD' })))
        cl_action.CommonClearOnePlant(oWarrior, oEventCB.GetCBLifeCycle())
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 138, 0, 0, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func377(*a)), CURE_TYPE_PERFORM | DAM_USE_ALL, 0, 0, 0)
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'PlanPhase') == 2:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33783, 0, {
            'SneerCD': (lambda *a: Func717(*a, **{
'sArg': 'TreeSneerCD' })),
            'SneerRange': (lambda *a: Func717(*a, **{
'sArg': 'TreeSneerRange' })),
            'SneerTime': (lambda *a: Func717(*a, **{
'sArg': 'TreeSneerTime' })) }, 0, 0, 0)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33783, 0, {
            'SneerCD': (lambda *a: Func717(*a, **{
'sArg': 'PlantSneerCD' })),
            'SneerRange': (lambda *a: Func717(*a, **{
'sArg': 'PlantSneerRange' })),
            'SneerTime': (lambda *a: Func717(*a, **{
'sArg': 'PlantSneerTime' })) }, 0, 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33784, 1, (lambda *a: Func717(*a, **{
'sArg': 'CountTime' })))
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AddShield' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33784, 1, (lambda *a: Func717(*a, **{
'sArg': 'CountTime' })))
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AddShield' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3805
    m_Name = '灵植庇护'
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
        2: DoCallBackAction2 }
    m_BaseArgData = {
        'Lv2TreeSneerCD': 600,
        'Lv2TreeSneerTime': 200,
        'Lv2TreeSneerRange': 8,
        'Lv3TreeSneerCD': 400,
        'Lv3TreeSneerTime': 300,
        'Lv3TreeSneerRange': 8,
        'Lv2PlantSneerCD': 600,
        'Lv2PlantSneerTime': 100,
        'Lv2PlantSneerRange': 5,
        'Lv3PlantSneerCD': 400,
        'Lv3PlantSneerTime': 150,
        'Lv3PlantSneerRange': 5,
        'LV3CD': 12000,
        'LV1CountTime': 200,
        'LV2CountTime': 300,
        'LV3CountTime': 300,
        'LV1AddMax': 1000,
        'LV2AddMax': 1500,
        'LV3AddMax': 2000,
        'LV1AddShield': 1000,
        'LV2AddShield': 1500,
        'LV3AddShield': 2000 }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 119

