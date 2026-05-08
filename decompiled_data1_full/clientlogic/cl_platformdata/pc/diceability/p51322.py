# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51322.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51322.pyc
# Source Generated with Decompyle++
# File: p51322.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO
from cl_newformula import Func717

def Action2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33686):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv2MaxBullet' })), 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33686, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv2MaxBullet' })), 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: -Func717(*a, **{
'sArg': 'Lv2MaxBullet' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 33686) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33686)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33686):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv3MaxBullet' })), 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33686, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv3MaxBullet' })), 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: -Func717(*a, **{
'sArg': 'Lv3MaxBullet' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 33686) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33686)


def Action4(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33686):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxBullet' })), 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33686, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxBullet' })), 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: -Func717(*a, **{
'sArg': 'Lv4MaxBullet' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 33686) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33686)


def Action5(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33686):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxBullet' })), 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33686, 0, { }, 0)
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: Func717(*a, **{
'sArg': 'Lv5MaxBullet' })), 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33686, (lambda *a: -Func717(*a, **{
'sArg': 'Lv5MaxBullet' })), 0)
    if cl_condition.GetStateCount(oWarrior, oLifeCycle, 33686) <= 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33686)


class CPerform(CCustomPerform):
    m_SID = 51322
    m_Name = '爆射'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'Lv2MaxBullet': 3,
        'Lv3MaxBullet': 4,
        'Lv4MaxBullet': 6,
        'Lv5MaxBullet': 10 }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

