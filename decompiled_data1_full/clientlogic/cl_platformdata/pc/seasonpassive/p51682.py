# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51682.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51682.pyc
# Source Generated with Decompyle++
# File: p51682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39777):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39777, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', (lambda *a: Func859(*a, **{
'sAttr': 'PerProb' })), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', (lambda *a: Func859(*a, **{
'sAttr': 'MaxProb' })), 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, 1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, -1, 0)


def Action2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39777):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39777, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', (lambda *a: Func859(*a, **{
'sAttr': 'PerProb' })), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', (lambda *a: Func859(*a, **{
'sAttr': 'MaxProb' })), 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, 1, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, -1, 0)


def Action3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39777):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39777, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', (lambda *a: Func859(*a, **{
'sAttr': 'PerProb' })), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', (lambda *a: Func859(*a, **{
'sAttr': 'MaxProb' })), 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, 1, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, -1, 0)


def Action4(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 39777):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 39777, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', (lambda *a: Func859(*a, **{
'sAttr': 'PerProb' })), 0, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', (lambda *a: Func859(*a, **{
'sAttr': 'MaxProb' })), 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, 1, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'PerProb', 0, 0)
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 39777, 'MaxProb', 0, 0)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 39777, -1, 0)


class CPerform(CCustomPerform):
    m_SID = 51682
    m_Name = '主要技能-法术暴击'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'PerProb': 1,
            'MaxProb': 10 },
        2: {
            'PerProb': 2,
            'MaxProb': 20 },
        3: {
            'PerProb': 3,
            'MaxProb': 36 },
        4: {
            'PerProb': 4,
            'MaxProb': 52 } }

