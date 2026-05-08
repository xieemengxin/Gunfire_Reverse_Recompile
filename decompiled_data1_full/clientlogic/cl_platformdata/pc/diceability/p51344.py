# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51344.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51344.pyc
# Source Generated with Decompyle++
# File: p51344.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_HP, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_MAINWEAPON, OBJ_ATTACK
from cl_newformula import Func509, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEff', 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, -1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCrazy', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEff', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, -1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCrazy', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHpMax', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEff', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33773, 0, {
        'ExtraHpMax': (lambda *a: Func717(*a, **{
'sArg': 'ExtraHpMax' })) }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, -1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCrazy', 8000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHpMax', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEff', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33773, 0, {
        'ExtraHpMax': (lambda *a: Func717(*a, **{
'sArg': 'ExtraHpMax' })) }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, -1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCrazy', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHpMax', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EffectTime', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'RecoveryEff', 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33773, 0, {
        'ExtraHpMax': (lambda *a: Func717(*a, **{
'sArg': 'ExtraHpMax' })) }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, -1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCrazy'), 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCrazy'), 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'Weakness', 0, 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func509(*a, **{
'sAttr': 'CrazyEff' }) / 100) * cl_evact.EventCBGetArgDataInCache(oWarrior, oEventCB, 'RecoveryEff')), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 0)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHpMax'):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33773, 1, 0, 1, cl_evact.EventCBGetArgDataInCache(oWarrior, oEventCB, 'EffectTime'))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Weakness', 1) and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'Weakness', 1, 1)


class CPerform(CCustomPerform):
    m_SID = 51344
    m_Name = '灵魂虹吸'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

