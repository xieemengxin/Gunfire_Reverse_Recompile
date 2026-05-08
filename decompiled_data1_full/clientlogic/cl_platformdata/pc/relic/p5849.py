# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5849.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5849.pyc
# Source Generated with Decompyle++
# File: p5849.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func410, Func518, Func598, Func610

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1531, 0, { }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'New5849' }))) == 0 and cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'Loading' }))):
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33501):
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1531, (lambda *a: 80 - Func610(*a, **{
'iStateSID': 33501,
'sKey': 'BuyGood' }) * 5), None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33501, 0, { }, 0)
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1531, (lambda *a: 80 - Func610(*a, **{
'iStateSID': 33501,
'sKey': 'BuyGood' }) * 5), None)
    cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'New5849', 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1556, 0, { }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'New5849' }))) == 0 and cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'Loading' }))):
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 2)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33501):
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1556, (lambda *a: (80 - Func610(*a, **{
'iStateSID': 33501,
'sKey': 'BuyGood' }) * 5) + Func610(*a, **{
'iStateSID': 33501,
'sKey': 'ShopNum' }) * 10), None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33501, 0, { }, 0)
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1556, (lambda *a: (80 - Func610(*a, **{
'iStateSID': 33501,
'sKey': 'BuyGood' }) * 5) + Func610(*a, **{
'iStateSID': 33501,
'sKey': 'ShopNum' }) * 10), None)
    cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'New5849', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1531 }))) > 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: ((Func410(*a, **{
'sid': 1531 }) - 80) % 10) // 5), 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: (Func410(*a, **{
'sid': 1531 }) - 80) // 10), 33501, 'ShopNum')
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1531 }))) == 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'ShopNum')
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1531 }))) < 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: (80 - Func410(*a, **{
'sid': 1531 })) // 5), 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'ShopNum')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1556 }))) > 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: ((Func410(*a, **{
'sid': 1556 }) - 80) % 10) // 5), 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: (Func410(*a, **{
'sid': 1556 }) - 80) // 10), 33501, 'ShopNum')
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1556 }))) == 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'ShopNum')
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func410(*a, **{
'sid': 1556 }))) < 80:
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: (80 - Func410(*a, **{
'sid': 1556 })) // 5), 33501, 'BuyGood')
        cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, 0, 33501, 'ShopNum')


class CPerform(CCustomPerform):
    m_SID = 5849
    m_Name = '理性消费'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

