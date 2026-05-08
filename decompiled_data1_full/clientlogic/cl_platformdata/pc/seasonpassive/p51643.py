# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51643.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51643.pyc
# Source Generated with Decompyle++
# File: p51643.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func746, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 200)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39699, 0, {
        'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 400)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39699, 0, {
        'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDamRatio', 10)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39699, 0, {
        'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })),
        'ExtraDamRatio': (lambda *a: Func717(*a, **{
'sArg': 'ExtraDamRatio' })) }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMainPerform(oWarrior, oEventCB, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39697, 1, 1, 0):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39697, 1, 1, 1, None)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 39697, 0, { }, 1, 1, 0)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraDamRatio'):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, (lambda *a: (Func717(*a, **{
'sArg': 'DamRatio' }) + Func746(*a, **{
'iStateSID': 39699 }) * Func717(*a, **{
'sArg': 'ExtraDamRatio' })) * cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 39697, 1, 1)), 0, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' }) * cl_evact.EventCBGetTargetStateCount(oWarrior, oEventCB, 39697, 1, 1)), 0, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39699, (lambda *a: Func839(*a)), 1)


class CPerform(CCustomPerform):
    m_SID = 51643
    m_Name = '魔法风暴迭代'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

