# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51307.pyc
# Source Generated with Decompyle++
# File: p51307.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRatio', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRatio', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRatio', 6000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33763, 0, {
        'BagBulletRecoveryRatio': 2 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRatio', 9000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33763, 0, {
        'BagBulletRecoveryRatio': 4,
        'BulletRecoveryRatio': 5,
        'StatusEffect': 1 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BulletRatio', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxBagBulletRatio', 5000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33763, 0, {
        'BagBulletRecoveryRatio': 6,
        'BulletRecoveryRatio': 10,
        'StatusEffect': 1 }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4502, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4503, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4504, (lambda *a: Func717(*a, **{
'sArg': 'MaxBagBulletRatio' })), 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'MaxBullet', 0, (lambda *a: Func717(*a, **{
'sArg': 'BulletRatio' })), 0, { })


class CPerform(CCustomPerform):
    m_SID = 51307
    m_Name = '扩容弹夹'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

