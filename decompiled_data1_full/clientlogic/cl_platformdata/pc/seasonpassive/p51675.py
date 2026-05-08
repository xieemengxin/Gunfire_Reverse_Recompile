# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51675.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51675.pyc
# Source Generated with Decompyle++
# File: p51675.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2007)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51587AoeRange', (lambda *a: Func717(*a, **{
'sArg': 'AoeRange' })))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'AttRatio', (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' })), 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2007)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51587AoeRange', (lambda *a: Func717(*a, **{
'sArg': 'AoeRange' })))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'AttRatio', (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' })), 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2007)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51587AoeRange', (lambda *a: Func717(*a, **{
'sArg': 'AoeRange' })))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'AttRatio', (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchDis', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchDis' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAtt', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAtt' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAoeRange', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAoeRange' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAoeAtt', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAoeAtt' })), 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2007)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51587AoeRange', (lambda *a: Func717(*a, **{
'sArg': 'AoeRange' })))
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'AttRatio', (lambda *a: Func859(*a, **{
'sAttr': 'AttRatio' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchDis', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchDis' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAtt', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAtt' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAoeRange', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAoeRange' })), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 2007, 'LaunchAoeAtt', (lambda *a: Func859(*a, **{
'sAttr': 'LaunchAoeAtt' })), 1)


class CPerform(CCustomPerform):
    m_SID = 51675
    m_Name = '雷刃-爆破雷刃'
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
        'AoeRange': 30 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'AttRatio': 400 },
        2: {
            'AttRatio': 800 },
        3: {
            'AttRatio': 1200,
            'LaunchAtt': 6000,
            'LaunchDis': 10,
            'LaunchAoeRange': 50,
            'LaunchAoeAtt': 2000 },
        4: {
            'AttRatio': 1600,
            'LaunchAtt': 10000,
            'LaunchDis': 10,
            'LaunchAoeRange': 50,
            'LaunchAoeAtt': 2500 } }

