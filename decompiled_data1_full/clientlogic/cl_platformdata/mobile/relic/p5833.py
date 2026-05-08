# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5833.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5833.pyc
# Source Generated with Decompyle++
# File: p5833.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, SMITHNPCSUBMSG_UPGRADE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddWeaponUpgradeCnt(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddWeaponUpgradeLevel(oWarrior, oEventCB, 1)


class CPerform(CCustomPerform):
    m_SID = 5833
    m_Name = '幕后交易'
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
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

