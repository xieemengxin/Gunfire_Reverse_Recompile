# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5884.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5884.pyc
# Source Generated with Decompyle++
# File: p5884.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func247, Func430, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'P5884_TIME', (lambda *a: Func430(*a, **{
'sid': 32404 })))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'P5884_TIME', (lambda *a: Func430(*a, **{
'sid': 32404 })))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func247(*a))) != cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'LEVEL5884_1' }))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32404, 4000, { }, 1, 0, 0)
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'LEVEL5884_1', (lambda *a: Func247(*a)), 1)
    elif cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'P5884_TIME') > 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32404, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'P5884_TIME'), { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func247(*a))) != cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func598(*a, **{
'sKey': 'LEVEL5884_2' }))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32404, 4000, {
            'StatusEffect': 1 }, 1, 0, 0)
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'LEVEL5884_2', (lambda *a: Func247(*a)), 1)
    elif cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'P5884_TIME') > 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32404, cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'P5884_TIME'), {
            'StatusEffect': 1 }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5884
    m_Name = '争分夺秒'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_NORMAL

