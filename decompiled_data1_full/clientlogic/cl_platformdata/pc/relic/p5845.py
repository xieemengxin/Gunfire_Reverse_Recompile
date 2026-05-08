# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5845.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5845.pyc
# Source Generated with Decompyle++
# File: p5845.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import MG_SOURCE_RELIC, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5845)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5845)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5845, None)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })
    cl_action.CommonRandomReduceTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2)
    cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2412, {
        4: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
    cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2413, {
        1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5845, None)
    cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DESTROY_RELIC, -1, { })
    cl_action.CommonRandomReduceTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), 2)
    cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2412, {
        2: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
    cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2413, {
        3: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5845
    m_Name = '抛砖引玉'
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
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 120
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

