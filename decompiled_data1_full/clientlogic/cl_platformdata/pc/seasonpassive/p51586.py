# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51586.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51586.pyc
# Source Generated with Decompyle++
# File: p51586.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33928, 0, {
        'UseWinkCnt': 3,
        'MaxCount': 5,
        'Distance': 25,
        'AttRatio': 8,
        'FireRing': 0,
        'BaseAtt': 40000,
        'PerRatio': 50,
        'AIDamFactor': 1000 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33928, 0, {
        'UseWinkCnt': 3,
        'MaxCount': 5,
        'Distance': 25,
        'AttRatio': 16,
        'FireRing': 0,
        'BaseAtt': 80000,
        'PerRatio': 100,
        'AIDamFactor': 2000 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33928, 0, {
        'UseWinkCnt': 3,
        'MaxCount': 5,
        'Distance': 25,
        'AttRatio': 24,
        'FireRing': 0,
        'BaseAtt': 160000,
        'PerRatio': 200,
        'AIDamFactor': 3000 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33928, 0, {
        'UseWinkCnt': 2,
        'MaxCount': 5,
        'Distance': 20,
        'AttRatio': 32,
        'FireRing': 1,
        'BaseAtt': 240000,
        'PerRatio': 400,
        'AIDamFactor': 4000 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33928, 0, {
        'UseWinkCnt': 2,
        'MaxCount': 8,
        'Distance': 20,
        'AttRatio': 40,
        'FireRing': 1,
        'BaseAtt': 320000,
        'PerRatio': 600,
        'AIDamFactor': 5000 }, 1)


class CPerform(CCustomPerform):
    m_SID = 51586
    m_Name = '#NT#流星'
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

