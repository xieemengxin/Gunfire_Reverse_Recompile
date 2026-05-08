# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51368.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51368.pyc
# Source Generated with Decompyle++
# File: p51368.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, NORMAL_DAMAGE, OBJ_SELF
from cl_newformula import Func304, Func717

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SelfDamRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverHP', 40)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SelfDamRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverHP', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HPMaxAdd', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxHpEffect', 90)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SelfDamRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverHP', 80)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HPMaxAdd', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxHpEffect', 180)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SelfDamRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'IntervalTime', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 1200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoverHP', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HPMaxAdd', 120)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxHpEffect', 360)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min(int(Func304(*a, **{
'sAttr': 'HPMax' }) * Func717(*a, **{
'sArg': 'SelfDamRatio' }) // 100), int(Func304(*a, **{
'sAttr': 'HP' }) - 1))), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP, 0, 0, 1, 0, 0, 0, 0, 0, NORMAL_DAMAGE, 0, 0)
    cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })), 0, 0, 1, 1)
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33818, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' }) + 4), {
        'IntervalTime': (lambda *a: Func717(*a, **{
'sArg': 'IntervalTime' })),
        'RecoverHP': (lambda *a: Func717(*a, **{
'sArg': 'RecoverHP' })),
        'HPMaxAdd': (lambda *a: Func717(*a, **{
'sArg': 'HPMaxAdd' })),
        'MaxHpEffect': (lambda *a: Func717(*a, **{
'sArg': 'MaxHpEffect' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51368
    m_Name = '血契魔法'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

