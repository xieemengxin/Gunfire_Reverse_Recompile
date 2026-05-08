# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5822.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5822.pyc
# Source Generated with Decompyle++
# File: p5822.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import MG_SOURCE_RELIC, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5822, 0)
    cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'PF5822', 1, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'PF5822' }))) >= 3:
        cl_action.CommonAddFilterRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5822)
    cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2408, {
        2: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5822, 0)
    cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'PF5822', 1, 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'PF5822' }))) >= 3:
        cl_action.CommonAddFilterRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5822)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2408, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 2, None)
    else:
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2408, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2408, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 2, None)
    else:
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2408, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5822
    m_Name = '有效分裂'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 120
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

