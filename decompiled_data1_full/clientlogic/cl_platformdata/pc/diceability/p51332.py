# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51332.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51332.pyc
# Source Generated with Decompyle++
# File: p51332.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_ONE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33743, 0, {
        'GainEffect': 1000,
        'StatusEffect': 8 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33743, 0, {
        'GainEffect': 1500,
        'StatusEffect': 12 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33743, 0, {
        'DamReduce': 2000,
        'GainEffect': 2000,
        'StatusEffect': 12 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33743, 0, {
        'GainEffect': 3000,
        'StatusEffect': 12,
        'DamReduce': 3000 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33743, 0, {
        'GainEffect': 5000,
        'StatusEffect': 16,
        'DamReduce': 5000 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33744, 0, {
        'iDiceSID': 51332 }, 1)
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33744):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33744, 0, {
            'iDiceSID': 51332 }, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33744, 1, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33744, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51332
    m_Name = '近战大师'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

