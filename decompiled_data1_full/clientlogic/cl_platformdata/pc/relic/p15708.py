# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p15708.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p15708.pyc
# Source Generated with Decompyle++
# File: p15708.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 1, 0, 0)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', -5000, 0, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GETWARCASH, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeGetCash(oWarrior, oEventCB, 1000, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBChangeGetCash(oWarrior, oEventCB, 1000, 0)


class CPerform(CCustomPerform):
    m_SID = 15708
    m_Name = '魔鬼契约'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

