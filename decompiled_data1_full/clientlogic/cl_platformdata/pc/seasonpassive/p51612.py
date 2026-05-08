# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51612.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51612.pyc
# Source Generated with Decompyle++
# File: p51612.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39674, 0, {
        'MaxCount': 10,
        'Duration': 500,
        'DamRatio': 3 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39674, 0, {
        'MaxCount': 10,
        'Duration': 500,
        'DamRatio': 5 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39674, 0, {
        'MaxCount': 10,
        'Duration': 500,
        'DamRatio': 8,
        'AbsorbThress': 7 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39674, 0, {
        'MaxCount': 10,
        'Duration': 500,
        'DamRatio': 10,
        'AbsorbThress': 5 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51612
    m_Name = '莲花-次要技能伤害'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

