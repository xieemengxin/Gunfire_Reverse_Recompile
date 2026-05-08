# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51904.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51904.pyc
# Source Generated with Decompyle++
# File: p51904.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Att', (lambda *a: Func859(*a, **{
'sAttr': 'Att' })))
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Radius', (lambda *a: Func859(*a, **{
'sAttr': 'Redius' })))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Att', (lambda *a: Func859(*a, **{
'sAttr': 'Att' })))
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Radius', (lambda *a: Func859(*a, **{
'sAttr': 'Redius' })))


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Att', (lambda *a: Func859(*a, **{
'sAttr': 'Att' })))
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 52004, 'Radius', (lambda *a: Func859(*a, **{
'sAttr': 'Redius' })))


class CPerform(CCustomPerform):
    m_SID = 51904
    m_Name = '鱼龙'
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
            'Att': 100000,
            'Redius': 5 },
        2: {
            'Att': 200000,
            'Redius': 5 },
        3: {
            'Att': 300000,
            'Redius': 5 } }

