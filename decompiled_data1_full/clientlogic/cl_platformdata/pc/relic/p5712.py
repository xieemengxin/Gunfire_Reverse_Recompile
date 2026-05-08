# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5712.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5712.pyc
# Source Generated with Decompyle++
# File: p5712.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Shield() <= 0 and oWarrior.Armor() <= 0 and oWarrior.GetShieldStatus() == 0:
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1108, 0, { }, 1)
    elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1108):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1108, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1108):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1108, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if oWarrior.Shield() <= 0 and oWarrior.Armor() <= 0 and oWarrior.GetShieldStatus() == 0:
        if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1370):
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1370, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1369, 0, { }, 1)
    elif cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1369):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1369, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1370, 1000, { }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1369):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1369, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1370, 1000, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5712
    m_Name = '破釜沉舟'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

