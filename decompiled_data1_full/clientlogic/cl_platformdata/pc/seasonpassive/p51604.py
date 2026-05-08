# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51604.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51604.pyc
# Source Generated with Decompyle++
# File: p51604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33961, 0, {
        'ProbCrazyEff': 0,
        'AddCrazyEff': 500 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33961, 0, {
        'ProbCrazyEff': 5,
        'AddCrazyEff': 1000 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33961, 0, {
        'ProbCrazyEff': 10,
        'AddCrazyEff': 2000 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33961, 0, {
        'ProbCrazyEff': 20,
        'AddCrazyEff': 2500 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51604
    m_Name = '#NT#低频暴击'
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

