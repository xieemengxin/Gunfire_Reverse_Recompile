# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51670.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51670.pyc
# Source Generated with Decompyle++
# File: p51670.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39760, 0, {
        'NpcHP': (lambda *a: Func859(*a, **{
'sAttr': 'NpcHP' })),
        'EliteHP': (lambda *a: Func859(*a, **{
'sAttr': 'EliteHP' })),
        'BossHP': (lambda *a: Func859(*a, **{
'sAttr': 'BossHP' })),
        'PerShieldAndArmor': (lambda *a: Func859(*a, **{
'sAttr': 'PerShieldAndArmor' })),
        'MaxDamRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxDamRate' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39760, 0, {
        'NpcHP': (lambda *a: Func859(*a, **{
'sAttr': 'NpcHP' })),
        'EliteHP': (lambda *a: Func859(*a, **{
'sAttr': 'EliteHP' })),
        'BossHP': (lambda *a: Func859(*a, **{
'sAttr': 'BossHP' })),
        'PerShieldAndArmor': (lambda *a: Func859(*a, **{
'sAttr': 'PerShieldAndArmor' })),
        'MaxDamRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxDamRate' })) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39760, 0, {
        'NpcHP': (lambda *a: Func859(*a, **{
'sAttr': 'NpcHP' })),
        'EliteHP': (lambda *a: Func859(*a, **{
'sAttr': 'EliteHP' })),
        'BossHP': (lambda *a: Func859(*a, **{
'sAttr': 'BossHP' })),
        'PerShieldAndArmor': (lambda *a: Func859(*a, **{
'sAttr': 'PerShieldAndArmor' })),
        'MaxDamRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxDamRate' })) }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39760, 0, {
        'NpcHP': (lambda *a: Func859(*a, **{
'sAttr': 'NpcHP' })),
        'EliteHP': (lambda *a: Func859(*a, **{
'sAttr': 'EliteHP' })),
        'BossHP': (lambda *a: Func859(*a, **{
'sAttr': 'BossHP' })),
        'PerShieldAndArmor': (lambda *a: Func859(*a, **{
'sAttr': 'PerShieldAndArmor' })),
        'MaxDamRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxDamRate' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 51670
    m_Name = '主要技能-透骨罡气'
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
        'StateTime': 5,
        'PerDamRate': 10 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'BossHP': 15,
            'EliteHP': 60,
            'NpcHP': 200,
            'MaxDamRate': 120,
            'PerShieldAndArmor': 40 },
        2: {
            'BossHP': 30,
            'EliteHP': 120,
            'NpcHP': 400,
            'MaxDamRate': 120,
            'PerShieldAndArmor': 40 },
        3: {
            'BossHP': 45,
            'EliteHP': 180,
            'NpcHP': 600,
            'MaxDamRate': 160,
            'PerShieldAndArmor': 30 },
        4: {
            'BossHP': 60,
            'EliteHP': 240,
            'NpcHP': 800,
            'MaxDamRate': 200,
            'PerShieldAndArmor': 30 } }

