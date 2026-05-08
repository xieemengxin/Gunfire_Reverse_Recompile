# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51209.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51209.pyc
# Source Generated with Decompyle++
# File: p51209.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func354, Func361, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32524, 0, {
        'CoastRatio': (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'CoastRatio' })) }, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51209, 'LevelMul', (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'Level1Mul' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33634, 0, {
        'StateCount': 60 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32524, 0, {
        'CoastRatio': (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'CoastRatio' })) }, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51209, 'LevelMul', (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'Level2Mul' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33634, 0, {
        'StateCount': 60 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32524, 0, {
        'CoastRatio': (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'CoastRatio' })) }, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 51209, 'LevelMul', (lambda *a: Func361(*a, **{
'sid': 51209,
'sArgs': 'Level3Mul' })), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33634, 0, {
        'StateCount': 60 }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func354(*a))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 7952, 0, 0, 0, 0) or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 1206, 0, 0, 0, 0) or cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 51209, 0, 0):
            cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'w1010_Dam', (lambda *a: Func354(*a) * Func361(*a, **{
'sid': 51209,
'sArgs': 'LevelMul' }) / 10000), 1)
            cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) // 100))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) // 100))


class CPerform(CCustomPerform):
    m_SID = 51209
    m_Name = '#NT#印记法杖被动'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = {
        'Level1Mul': 6000,
        'Level2Mul': 8000,
        'Level3Mul': 10000,
        'CoastRatio': 2000 }
    m_DieDisable = 0

