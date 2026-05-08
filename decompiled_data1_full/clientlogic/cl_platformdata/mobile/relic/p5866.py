# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5866.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5866.pyc
# Source Generated with Decompyle++
# File: p5866.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL, SMITHNPCSUBMSG_UPGRADE
from cl_newformula import Func240

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 0, 0, 0)
    cl_action.CommonForceSetOwnerWeaponUpgradeUnlimit(oWarrior, oLifeCycle, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 4, 0, 0)
    cl_action.CommonForceSetOwnerWeaponUpgradeUnlimit(oWarrior, oLifeCycle, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func240(*a)), 1)
    if cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func240(*a))) >= 3:
        cl_evact.EventCBSetSmithExtraUpgradeCost(oWarrior, oEventCB, 130)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetSmithExtraUpgradeCostEnable(oWarrior, oEventCB, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetSmithExtraUpgradeCostEnable(oWarrior, oEventCB, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func240(*a)), 1)
    if cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func240(*a))) >= 3:
        cl_evact.EventCBSetSmithExtraUpgradeCost(oWarrior, oEventCB, 100)


class CPerform(CCustomPerform):
    m_SID = 5866
    m_Name = '额外服务'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

