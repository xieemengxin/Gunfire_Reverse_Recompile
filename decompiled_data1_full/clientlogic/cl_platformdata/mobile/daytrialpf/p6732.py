# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6732.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6732.pyc
# Source Generated with Decompyle++
# File: p6732.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func207, Func304, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1264, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1270, 0, { }, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1296, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) / 30)) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) / 100 + Func410(*a, **{
'sid': 1264 }))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: (-Func207(*a) / 30) * 100), 0)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1264, (lambda *a: Func207(*a) / 30))
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func207(*a) / 30))
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', 0, 0)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', 0, 0)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1264, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) / 100 - 1), 0)
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: -Func410(*a, **{
'sid': 1264 }) * 100), 0)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: max(Func304(*a, **{
'sAttr': 'ShieldMax' }), Func304(*a, **{
'sAttr': 'ArmorMax' })) + Func410(*a, **{
'sid': 1270 }) * 100)) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func207(*a) / 30) * 100 - Func410(*a, **{
'sid': 1264 }) * 100)):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1270, (lambda *a: max(Func304(*a, **{
'sAttr': 'ShieldMax' }), Func304(*a, **{
'sAttr': 'ArmorMax' })) / 100 - 1), 0)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: -Func410(*a, **{
'sid': 1270 }) * 100), 0)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: -Func410(*a, **{
'sid': 1270 }) * 100), 0)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func410(*a, **{
'sid': 1264 })))
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func410(*a, **{
'sid': 1270 })), 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1270, (lambda *a: Func207(*a) / 30 - Func410(*a, **{
'sid': 1264 })))
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: Func410(*a, **{
'sid': 1264 }) * 100 - (Func207(*a) / 30) * 100), 0)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: Func410(*a, **{
'sid': 1264 }) * 100 - (Func207(*a) / 30) * 100), 0)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func207(*a) / 30))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5703):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a) / 30)) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) / 100 + Func410(*a, **{
'sid': 1264 }))):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: (-Func207(*a) / 30) * 100), 0)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1264, (lambda *a: Func207(*a) / 30))
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func207(*a) / 30))
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', 0, 0)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', 0, 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1264, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) / 100 - 1), 0)
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', (lambda *a: -Func410(*a, **{
'sid': 1264 }) * 100), 0)
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: max(Func304(*a, **{
'sAttr': 'ShieldMax' }), Func304(*a, **{
'sAttr': 'ArmorMax' })) + Func410(*a, **{
'sid': 1270 }) * 100)) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: (Func207(*a) / 30) * 100 - Func410(*a, **{
'sid': 1264 }) * 100)):
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1270, (lambda *a: max(Func304(*a, **{
'sAttr': 'ShieldMax' }), Func304(*a, **{
'sAttr': 'ArmorMax' })) / 100 - 1), 0)
                cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: -Func410(*a, **{
'sid': 1270 }) * 100), 0)
                cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: -Func410(*a, **{
'sid': 1270 }) * 100), 0)
                cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func410(*a, **{
'sid': 1264 })))
                cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func410(*a, **{
'sid': 1270 })), 0)
            else:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1270, (lambda *a: Func207(*a) / 30 - Func410(*a, **{
'sid': 1264 })))
                cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ShieldMax', (lambda *a: Func410(*a, **{
'sid': 1264 }) * 100 - (Func207(*a) / 30) * 100), 0)
                cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'ArmorMax', (lambda *a: Func410(*a, **{
'sid': 1264 }) * 100 - (Func207(*a) / 30) * 100), 0)
                cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1296, (lambda *a: Func207(*a) / 30))


class CPerform(CCustomPerform):
    m_SID = 6732
    m_Name = '玩家生命随铜币数量增加而减少'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

