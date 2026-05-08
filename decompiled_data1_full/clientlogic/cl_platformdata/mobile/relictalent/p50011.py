# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50011.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50011.pyc
# Source Generated with Decompyle++
# File: p50011.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', (lambda *a: -Func361(*a, **{
'sid': 50011,
'sArgs': 'Level1BaseReduceTime' })), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level1ExtraCDReduce'), None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', (lambda *a: -Func361(*a, **{
'sid': 50011,
'sArgs': 'Level2BaseReduceTime' })), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level2ExtraCDReduce'), None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', (lambda *a: -Func361(*a, **{
'sid': 50011,
'sArgs': 'Level3BaseReduceTime' })), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level3ExtraCDReduce'), None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level1BaseReduceTime'), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level1ExtraCDReduce'), None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level2BaseReduceTime'), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level2ExtraCDReduce'), None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDTime', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level3BaseReduceTime'), None)
    cl_action.CommonAddPerformArgsValue(oWarrior, oEventCB.GetCBLifeCycle(), 50014, 'CDReduce', -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Level3ExtraCDReduce'), None)


class CPerform(CCustomPerform):
    m_SID = 50011
    m_Name = '源能充盈'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = {
        'Level1BaseReduceTime': 300,
        'Level2BaseReduceTime': 500,
        'Level3BaseReduceTime': 700,
        'Level1ExtraCDReduce': 10,
        'Level2ExtraCDReduce': 20,
        'Level3ExtraCDReduce': 30 }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

