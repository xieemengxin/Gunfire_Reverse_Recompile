# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51589.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51589.pyc
# Source Generated with Decompyle++
# File: p51589.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import AFTER_ADDCOUNT, BEFORE_ADDCOUNT, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_VICTIM
from cl_newformula import Func651, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, BEFORE_ADDCOUNT, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prob', (lambda *a: Func717(*a, **{
'sArg': 'Lv1Prob' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, BEFORE_ADDCOUNT, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prob', (lambda *a: Func717(*a, **{
'sArg': 'Lv2Prob' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, BEFORE_ADDCOUNT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, AFTER_ADDCOUNT, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prob', (lambda *a: Func717(*a, **{
'sArg': 'Lv3Prob' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv3AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraElementCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv3ExtraElementCD' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992DeBuffMul', (lambda *a: Func717(*a, **{
'sArg': 'Lv3DeBuffDamMul' })))


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, BEFORE_ADDCOUNT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_FOGPOISON, AFTER_ADDCOUNT, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Prob', (lambda *a: Func717(*a, **{
'sArg': 'Lv4Prob' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv4AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraElementCD', (lambda *a: Func717(*a, **{
'sArg': 'Lv4ExtraElementCD' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992DeBuffMul', (lambda *a: Func717(*a, **{
'sArg': 'Lv4DeBuffDamMul' })))


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20027, 0, 0, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, (lambda *a: Func717(*a, **{
'sArg': 'Prob' }))):
        cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'AddCount', (lambda *a: Func651(*a, **{
'sKey': 'AddCount' }) + 1))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'OldCount' }))) >= 5:
        cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 2, (lambda *a: min(5, Func651(*a, **{
'sKey': 'AddCount' }))), None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'ExtraElementCD' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 3400,
            4: 3300,
            5: 3300 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, DAM_TYPE_FIRE, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, DAM_TYPE_CORRISION, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, DAM_TYPE_THUNDER, 0)


class CPerform(CCustomPerform):
    m_SID = 51589
    m_Name = '#NT#毒雾频率组件'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'Lv1Prob': 20,
        'Lv2Prob': 30,
        'Lv3AddDam': 4000,
        'Lv3DeBuffDamMul': 4000,
        'Lv3ExtraElementCD': 25,
        'Lv3Prob': 40,
        'Lv4AddDam': 8000,
        'Lv4DeBuffDamMul': 8000,
        'Lv4ExtraElementCD': 25,
        'Lv4Prob': 50 }
    m_DieDisable = 0

