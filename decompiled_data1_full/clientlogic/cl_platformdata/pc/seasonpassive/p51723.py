# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51723.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51723.pyc
# Source Generated with Decompyle++
# File: p51723.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39772, 0, {
        'PerMax': (lambda *a: Func859(*a, **{
'sAttr': 'PerMax' })),
        'RangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'RangeMul' })),
        'MaxRangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRangeMul' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39772, 0, {
        'PerMax': (lambda *a: Func859(*a, **{
'sAttr': 'PerMax' })),
        'RangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'RangeMul' })),
        'MaxRangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRangeMul' })) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39772, 0, {
        'PerMax': (lambda *a: Func859(*a, **{
'sAttr': 'PerMax' })),
        'RangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'RangeMul' })),
        'MaxRangeMul': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRangeMul' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51723
    m_Name = '次要范围'
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
            'PerMax': 10,
            'RangeMul': 2000,
            'MaxRangeMul': 3000 },
        2: {
            'PerMax': 10,
            'RangeMul': 4000,
            'MaxRangeMul': 6000 },
        3: {
            'PerMax': 10,
            'RangeMul': 8000,
            'MaxRangeMul': 12000 } }

