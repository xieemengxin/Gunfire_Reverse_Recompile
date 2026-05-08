# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25822.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25822.pyc
# Source Generated with Decompyle++
# File: p25822.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import MG_SOURCE_RELIC, QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonSetWeightDropGoods(oWarrior, oLifeCycle, 2408, {
        2: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5822, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5822, None)
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
    m_SID = 25822
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
    m_RelicType = 0
    m_HeroRelic = 5822
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

