# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5715.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5715.pyc
# Source Generated with Decompyle++
# File: p5715.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, DAM_TYPE_ELEMENT, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 2500, 0, DAM_TYPE_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 1, None, None, None, None)
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 0, 0, { }, 0, DAM_MASK_ELEMENT, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_MONSTER, 1, 0, 0, None, None, None, None)
    cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 0, 0, { }, 0, DAM_MASK_ELEMENT, None)


class CPerform(CCustomPerform):
    m_SID = 5715
    m_Name = '元素奥能'
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
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

