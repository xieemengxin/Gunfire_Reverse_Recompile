# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5776.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5776.pyc
# Source Generated with Decompyle++
# File: p5776.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableRelicByType(oWarrior, oEventCB, RELIC_TYPE_CURSE, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableRelicByType(oWarrior, oEventCB, RELIC_TYPE_CURSE, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetCurseRelicValidRemove(oWarrior, oEventCB)
    cl_evact.PassiveCBDisableRelicByType(oWarrior, oEventCB, RELIC_TYPE_CURSE, 1)


class CPerform(CCustomPerform):
    m_SID = 5776
    m_Name = '驱邪护符'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

