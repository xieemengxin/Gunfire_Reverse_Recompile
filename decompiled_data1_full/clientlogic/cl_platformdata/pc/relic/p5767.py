# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5767.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5767.pyc
# Source Generated with Decompyle++
# File: p5767.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DAM_TYPE_WEAPON, OBJ_ATTACK, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 12)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 20)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, -2000, 0, DAM_TYPE_WEAPON, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 20)
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        3: 2000 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) == 0:
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_WEAKNESS)


class CPerform(CCustomPerform):
    m_SID = 5767
    m_Name = '随缘枪法'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

