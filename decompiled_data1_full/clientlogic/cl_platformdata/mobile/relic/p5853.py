# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5853.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5853.pyc
# Source Generated with Decompyle++
# File: p5853.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_ATTACK, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func648

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 3, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON) == 0 and cl_evcon.CheckEventWeaponBulletType(oWarrior, oEventCB, 4503):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.GetTargetBagBulletAmount(oWarrior, oEventCB, 4504) >= cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4503):
            cl_evact.EventCBCostBagBulletByType(oWarrior, oEventCB, 4504, cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4503))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponBulletType(oWarrior, oEventCB, 4503):
        cl_evact.EventChangeDamCrazyEff(oWarrior, oEventCB, (lambda *a: Func648(*a) * 5000), 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON) == 0 and cl_evcon.CheckEventWeaponBulletType(oWarrior, oEventCB, 4503):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.GetTargetBagBulletAmount(oWarrior, oEventCB, 4504) >= cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4503) * 2):
            cl_evact.EventCBCostBagBulletByType(oWarrior, oEventCB, 4504, cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4503) * 2)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponBulletType(oWarrior, oEventCB, 4503):
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4503) * 30)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponBulletType(oWarrior, oEventCB, 4503):
        cl_evact.EventChangeDamCrazyEff(oWarrior, oEventCB, cl_evcon.GetBulletUseByType(oWarrior, oEventCB, 4504) * 5000, 0)


class CPerform(CCustomPerform):
    m_SID = 5853
    m_Name = '大号弹丸'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

