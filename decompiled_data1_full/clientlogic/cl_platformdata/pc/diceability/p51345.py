# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51345.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51345.pyc
# Source Generated with Decompyle++
# File: p51345.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_ONE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33774, 0, {
        'BaseLuckyHit': 20,
        'StatusEffect': 1 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33774, 0, {
        'BaseLuckyHit': 30,
        'StatusEffect': 2 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33774, 0, {
        'BaseLuckyHit': 40,
        'ExtraLuckyHit': 10,
        'EffectTime': 500,
        'MaxCount': 5,
        'StatusEffect': 3 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33774, 0, {
        'BaseLuckyHit': 60,
        'ExtraLuckyHit': 15,
        'EffectTime': 500,
        'MaxCount': 5,
        'StatusEffect': 4 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33774, 0, {
        'BaseLuckyHit': 100,
        'ExtraLuckyHit': 20,
        'EffectTime': 800,
        'MaxCount': 5,
        'StatusEffect': 5 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51345
    m_Name = '幸运一击'
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
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

