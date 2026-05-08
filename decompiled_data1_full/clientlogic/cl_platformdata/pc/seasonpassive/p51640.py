# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51640.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51640.pyc
# Source Generated with Decompyle++
# File: p51640.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_VICTIM
from cl_newformula import Func369, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Random', (lambda *a: Func717(*a, **{
'sArg': 'Lv1Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv1DamRatio' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Random', (lambda *a: Func717(*a, **{
'sArg': 'Lv2Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv2DamRatio' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Random', (lambda *a: Func717(*a, **{
'sArg': 'Lv3Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DouRandom', (lambda *a: Func717(*a, **{
'sArg': 'Lv3DouRandom' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv3DamRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DouDamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv3DouDamRatio' })))


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Random', (lambda *a: Func717(*a, **{
'sArg': 'Lv4Random' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DouRandom', (lambda *a: Func717(*a, **{
'sArg': 'Lv4DouRandom' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv4DamRatio' })))
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DouDamRatio', (lambda *a: Func717(*a, **{
'sArg': 'Lv4DouDamRatio' })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 10000, (lambda *a: Func717(*a, **{
'sArg': 'Random' }))) and cl_evcon.CheckMainPerform(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'DamRatio' }) / 10000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'DamRatio' }) / 10000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: 2 * Func369(*a) * Func717(*a, **{
'sArg': 'DouDamRatio' }) / 10000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckMainPerform(oWarrior, oEventCB, 0):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: (lambda *a: Func717(*a, **{
'sArg': 'Random' })),
            4: (lambda *a: Func717(*a, **{
'sArg': 'DouRandom' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51640
    m_Name = '技能连击'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'Lv1DamRatio': 3000,
        'Lv2DamRatio': 3000,
        'Lv3DamRatio': 3000,
        'Lv4DamRatio': 4000,
        'Lv1Random': 1500,
        'Lv2Random': 3000,
        'Lv3Random': 4000,
        'Lv4Random': 5000,
        'Lv3DouRandom': 800,
        'Lv4DouRandom': 1500,
        'Lv3DouDamRatio': 4000,
        'Lv4DouDamRatio': 4000 }
    m_DieDisable = 0

