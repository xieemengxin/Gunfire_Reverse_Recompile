# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5817.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5817.pyc
# Source Generated with Decompyle++
# File: p5817.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11045, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1269, 0, { }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 25)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB) and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventCBAddSourceWeaponBagBullet(oWarrior, oEventCB, 1)
        cl_evact.PassiveFillBullet(oWarrior, oEventCB, 1, 0)


class CPerform(CCustomPerform):
    m_SID = 5817
    m_Name = '备弹之光'
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
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

