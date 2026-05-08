# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5778.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5778.pyc
# Source Generated with Decompyle++
# File: p5778.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func340

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1167, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 4)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1167, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3333 }, None)
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf5778', None, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4502, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4503, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4504, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4502, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4503, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))
    cl_evact.EventAddBagBullet(oWarrior, oEventCB, 4504, (lambda *a: Func340(*a, **{
'sKey': 'pf5778' }) * 1 + 0))
    cl_evact.EventCBResetMoveDis(oWarrior, oEventCB, 'pf5778', None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5778
    m_Name = '刷步神器'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

