# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5860.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5860.pyc
# Source Generated with Decompyle++
# File: p5860.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.relic.customaction import CustomAction5860 as CustomAction
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1821) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1821, 0, { }, 1)
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'Exchange': 1 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1821) == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1821, 0, { }, 1)
    CustomAction(oWarrior, oEventCB.GetCBLifeCycle(), {
        'Exchange': 9,
        'Enhance': 1 })


class CPerform(CCustomPerform):
    m_SID = 5860
    m_Name = '幸运轮盘'
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
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

