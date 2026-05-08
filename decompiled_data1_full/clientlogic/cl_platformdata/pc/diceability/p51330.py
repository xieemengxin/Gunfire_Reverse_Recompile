# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51330.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51330.pyc
# Source Generated with Decompyle++
# File: p51330.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33720, 0, {
        'StateCount': 5,
        'DamRatio': 0.3,
        'DamTimes': 2,
        'Probability': 0 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33720, 0, {
        'StateCount': 5,
        'DamRatio': 0.4,
        'DamTimes': 3,
        'Probability': 0 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33720, 0, {
        'StateCount': 4,
        'DamRatio': 0.5,
        'DamTimes': 3,
        'Probability': 0 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33720, 0, {
        'StateCount': 4,
        'DamRatio': 0.5,
        'DamTimes': 4,
        'Probability': 5 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51330
    m_Name = '技能连击'
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
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

