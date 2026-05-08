# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51316.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51316.pyc
# Source Generated with Decompyle++
# File: p51316.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_OTHER, DICE_PUTOUT_POLL_ONE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'DamMul': 2500,
        'StatusEffect': 1 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'DamMul': 3500,
        'StatusEffect': 1 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'DamMul': 5000,
        'StatusEffect': 4 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'DamMul': 8000,
        'StatusEffect': 4 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33676, 0, {
        'DamMul': 12000,
        'StatusEffect': 4 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51316
    m_Name = '冲刺升级'
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
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

