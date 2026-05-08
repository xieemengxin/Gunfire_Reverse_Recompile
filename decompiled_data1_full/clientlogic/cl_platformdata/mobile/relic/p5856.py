# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5856.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5856.pyc
# Source Generated with Decompyle++
# File: p5856.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func522

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DYING, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DYING, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonSetDeadPunishmentTimes(oWarrior, oLifeCycle, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1794, 0, { }, 0, 1, None)
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 0, 0, 1, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1793, (lambda *a: Func522(*a) * 100 + 300), { }, 0, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1794, 0, { }, 0, 1, None)
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 0, 1, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1793, (lambda *a: Func522(*a) * 100 + 300), { }, 0, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetDeadPunishmentTimes(oWarrior, oEventCB.GetCBLifeCycle(), 0)


class CPerform(CCustomPerform):
    m_SID = 5856
    m_Name = '涅槃之力'
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
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

