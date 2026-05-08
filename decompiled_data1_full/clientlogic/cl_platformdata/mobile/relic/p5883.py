# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5883.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5883.pyc
# Source Generated with Decompyle++
# File: p5883.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonGetRelicByInfo(oWarrior, oLifeCycle, {
        RELIC_TYPE_NORMAL: 2,
        RELIC_TYPE_CURSE: 2 }, { }, {
        5883: 1,
        5823: 1,
        5822: 1,
        5845: 1 })
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonGetRelicByInfo(oWarrior, oLifeCycle, {
        RELIC_TYPE_NORMAL: 2,
        RELIC_TYPE_CURSE: 2 }, {
        RELIC_TYPE_NORMAL: 2 }, {
        5883: 1,
        5823: 1,
        5822: 1,
        5845: 1 })
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5883, 0)


class CPerform(CCustomPerform):
    m_SID = 5883
    m_Name = '#NT#混沌奖励'
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
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_NORMAL

