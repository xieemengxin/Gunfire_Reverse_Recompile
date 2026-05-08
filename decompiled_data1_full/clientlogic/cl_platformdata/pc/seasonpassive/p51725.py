# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51725.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51725.pyc
# Source Generated with Decompyle++
# File: p51725.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 220) or cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39770, 0, {
            'PerCost': (lambda *a: Func859(*a, **{
'sAttr': 'PerCost' })),
            'RecRatio': (lambda *a: Func859(*a, **{
'sAttr': 'RecRatio' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 220) or cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39770, 0, {
            'PerCost': (lambda *a: Func859(*a, **{
'sAttr': 'PerCost' })),
            'RecRatio': (lambda *a: Func859(*a, **{
'sAttr': 'RecRatio' })) }, 1)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 220) or cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39770, 0, {
            'PerCost': (lambda *a: Func859(*a, **{
'sAttr': 'PerCost' })),
            'RecRatio': (lambda *a: Func859(*a, **{
'sAttr': 'RecRatio' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51725
    m_Name = '英雄资源回复'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'PerCost': 10,
            'RecRatio': 30 },
        2: {
            'PerCost': 10,
            'RecRatio': 60 },
        3: {
            'PerCost': 10,
            'RecRatio': 120 } }

