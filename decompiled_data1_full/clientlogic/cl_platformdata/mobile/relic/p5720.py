# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5720.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5720.pyc
# Source Generated with Decompyle++
# File: p5720.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_MAINWEAPON, OBJ_ATTACK, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) == 0 and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -5000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'SnipeFov', 200, 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'SnipeFov', 200, 0, EQUIP_TYPE_FUNDAMENTALWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 20000, 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', 20000, 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


class CPerform(CCustomPerform):
    m_SID = 5720
    m_Name = '鹰眼瞄具'
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
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

