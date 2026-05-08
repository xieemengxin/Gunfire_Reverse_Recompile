# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51636.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51636.pyc
# Source Generated with Decompyle++
# File: p51636.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_VICTIM, S7_MODULE_POINT_CHANGE
from cl_newformula import Func308, Func369, Func717, Func839, Func840

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39711, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv1AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv1MaxAddDam' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_PERFORM, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39711, 0, { }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv2AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv2MaxAddDam' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_PERFORM, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 3, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39711, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'OneRandom', (lambda *a: Func717(*a, **{
'sArg': 'Lv3Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv3AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv3MaxAddDam' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_PERFORM, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 3, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39711, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'OneRandom', (lambda *a: Func717(*a, **{
'sArg': 'Lv4Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv4AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxAddDam' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_PERFORM, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 3, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39711, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'OneRandom', (lambda *a: Func717(*a, **{
'sArg': 'Lv5Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv5AddDam' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxAddDam', (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxAddDam' })))
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 3000, DAM_TYPE_PERFORM, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TotalAddDam' })), 0, DAM_TYPE_PERFORM, 1, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TotalAddDam', (lambda *a: min(Func839(*a) * Func717(*a, **{
'sArg': 'AddDam' }), Func717(*a, **{
'sArg': 'MaxAddDam' }))))
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
        'cdrate': (lambda *a: Func717(*a, **{
'sArg': 'TotalAddDam' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 39711)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 10000, (lambda *a: Func717(*a, **{
'sArg': 'Random' }))) and cl_evcon.CheckMainPerform(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TotalAddDam', (lambda *a: min(Func839(*a) * Func717(*a, **{
'sArg': 'AddDam' }), Func717(*a, **{
'sArg': 'MaxAddDam' }))))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Random', (lambda *a: Func717(*a, **{
'sArg': 'OneRandom' }) * Func840(*a)))
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func717(*a, **{
'sArg': 'Random' })),
        'cdrate': (lambda *a: Func717(*a, **{
'sArg': 'TotalAddDam' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 39711)


class CPerform(CCustomPerform):
    m_SID = 51636
    m_Name = '技能增幅'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'Lv1AddDam': 500,
        'Lv1MaxAddDam': 1500,
        'Lv2AddDam': 500,
        'Lv2MaxAddDam': 3000,
        'Lv3AddDam': 500,
        'Lv3MaxAddDam': 4500,
        'Lv4AddDam': 500,
        'Lv4MaxAddDam': 6000,
        'Lv5AddDam': 500,
        'Lv5MaxAddDam': 7500,
        'Lv3Random': 200,
        'Lv4Random': 500,
        'Lv5Random': 1000 }
    m_DieDisable = 0

