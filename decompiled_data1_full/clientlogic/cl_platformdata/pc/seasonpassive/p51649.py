# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51649.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51649.pyc
# Source Generated with Decompyle++
# File: p51649.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39715, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv1AddDam' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39715, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv2AddDam' })) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39715, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv3AddDam' })) }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39716, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv3MulDam' })),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'Lv3MaxCount' })) }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39715, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv4AddDam' })) }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39716, 0, {
        'AddDam': (lambda *a: Func717(*a, **{
'sArg': 'Lv4MulDam' })),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'Lv4MaxCount' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51649
    m_Name = '累计命中'
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
    m_BaseArgData = {
        'Lv1AddDam': 200,
        'Lv2AddDam': 400,
        'Lv3AddDam': 600,
        'Lv4AddDam': 800,
        'Lv3MaxCount': 15,
        'Lv4MaxCount': 10,
        'Lv3MulDam': 4000,
        'Lv4MulDam': 6000 }
    m_DieDisable = 0

