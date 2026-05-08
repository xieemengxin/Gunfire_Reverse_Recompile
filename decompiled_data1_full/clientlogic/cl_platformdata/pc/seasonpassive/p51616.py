# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51616.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51616.pyc
# Source Generated with Decompyle++
# File: p51616.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func247

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39678, 0, {
        'PerSecond': 1000,
        'BaseSpeedMul': 100,
        'MaxSpeedMul': 1000,
        'SpeedMulRatio': 40,
        'ThressHP': 20000,
        'PerThressHP': 5000 }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39678, 0, {
        'PerSecond': 1000,
        'BaseSpeedMul': 200,
        'MaxSpeedMul': 2000,
        'SpeedMulRatio': 40,
        'ThressHP': 20000,
        'PerThressHP': 5000 }, 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39678, 0, {
        'PerSecond': 1000,
        'BaseSpeedMul': 400,
        'MaxSpeedMul': 4000,
        'SpeedMulRatio': 40,
        'ThressHP': 20000,
        'PerThressHP': 5000 }, 1)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39678, 0, {
        'PerSecond': 1000,
        'BaseSpeedMul': 600,
        'MaxSpeedMul': 6000,
        'SpeedMulRatio': 60,
        'ThressHP': 20000,
        'PerThressHP': 5000 }, 1)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF51616', (lambda *a: Func247(*a)))


class CPerform(CCustomPerform):
    m_SID = 51616
    m_Name = '生存-战车'
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
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

