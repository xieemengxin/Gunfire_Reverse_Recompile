# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5858.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5858.pyc
# Source Generated with Decompyle++
# File: p5858.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func343, Func347

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func347(*a, **{
'sid': 4508 }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1801, 2000, { }, 1, 0, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1801, (lambda *a: Func343(*a, **{
'sid': 4508 })))
        cl_action.CommonModifyBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, (lambda *a: -Func343(*a, **{
'sid': 4508 })), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1801, 2000, { }, 1, 0, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1801, (lambda *a: Func343(*a, **{
'sid': 4508 })))
        cl_action.CommonModifyBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, (lambda *a: -Func343(*a, **{
'sid': 4508 })), 1)


class CPerform(CCustomPerform):
    m_SID = 5858
    m_Name = '水满则溢'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

