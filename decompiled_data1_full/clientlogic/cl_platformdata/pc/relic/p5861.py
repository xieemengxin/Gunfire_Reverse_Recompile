# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5861.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5861.pyc
# Source Generated with Decompyle++
# File: p5861.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1815, 0, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oWarrior, oEventCB):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1815, 0, { }, 1, 1, None)
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 7, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1070, 500, { }, 0, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5861
    m_Name = '慑敌之威'
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
    m_CycleTrigger = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

