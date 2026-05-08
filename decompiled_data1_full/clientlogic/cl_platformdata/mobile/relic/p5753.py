# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5753.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5753.pyc
# Source Generated with Decompyle++
# File: p5753.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EXECUTETYPE_RELICPF, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_BOSS, WARRIOR_NORBOX

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 8:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)
    elif cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 15 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 10:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)
    elif cl_evcon.GetVictimHPRatio(oWarrior, oEventCB) <= 20 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BOSS) == 0 and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_NORBOX) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTargetDeath(oWarrior, oEventCB, EXECUTETYPE_RELICPF)


class CPerform(CCustomPerform):
    m_SID = 5753
    m_Name = '终焉审判'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

