# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25845.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25845.pyc
# Source Generated with Decompyle++
# File: p25845.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MG_SOURCE_RELIC, QUALITY_TYPE_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonReduceTalentLevel(oWarrior, oLifeCycle, 0)
    cl_action.CommonSetWeightDropGoods(oWarrior, oLifeCycle, 2412, {
        4: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
    cl_action.CommonSetWeightDropGoods(oWarrior, oLifeCycle, 2413, {
        1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonReduceTalentLevel(oWarrior, oLifeCycle, 0)
    cl_action.CommonSetWeightDropGoods(oWarrior, oLifeCycle, 2412, {
        2: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
    cl_action.CommonSetWeightDropGoods(oWarrior, oLifeCycle, 2413, {
        3: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5845, None)


class CPerform(CCustomPerform):
    m_SID = 25845
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5845
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

