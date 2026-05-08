# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5786.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5786.pyc
# Source Generated with Decompyle++
# File: p5786.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ARMOR_RADIO_ADD, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, SHIELD_RADIO_ADD
from cl_newformula import Func314, Func582

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELDFINSH, -1, 1, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, ARMOR_RADIO_ADD, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, SHIELD_RADIO_ADD, 2)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELDFINSH, -1, 1, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, ARMOR_RADIO_ADD, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 100, SHIELD_RADIO_ADD, 2)
    cl_action.CommonForbid(oWarrior, oLifeCycle, 1041)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1168, 0, { }, 1, 0, None)
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 1811)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 1168)
    if cl_evcon.GetShieldRatio(oWarrior, oEventCB) == 100:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1811, 0, { }, 1, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func582(*a))) != -1:
        if cl_evcon.GetShieldRatio(oWarrior, oEventCB) == 100 or cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func314(*a))) == 1:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1811, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5786
    m_Name = '勃勃生机'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

