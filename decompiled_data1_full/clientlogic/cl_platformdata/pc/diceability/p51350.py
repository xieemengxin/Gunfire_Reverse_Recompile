# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51350.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51350.pyc
# Source Generated with Decompyle++
# File: p51350.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM
from cl_newformula import Func530, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ColdTime', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeed', 2000)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 1000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ColdTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeed', 3000)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 2000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ColdTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeed', 4000)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 3500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ColdTime', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeed', 5000)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeed', 6000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func530(*a))):
        cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, (lambda *a: -Func717(*a, **{
'sArg': 'ColdTime' })), 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33801, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), {
            'MoveSpeed': (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeed' })) }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSubCareerPerformColdTime(oWarrior, oEventCB, 0, -100)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -5000, 0, 'ReviceDam')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func530(*a))):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33801, (lambda *a: Func530(*a)), {
            'MoveSpeed': (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeed' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51350
    m_Name = '紧急避险'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

