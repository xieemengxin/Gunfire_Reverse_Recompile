# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5782.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5782.pyc
# Source Generated with Decompyle++
# File: p5782.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_ELEMENT, DAM_TYPE_THUNDER, FIGHT3_KEY_EVACT_IGNELETHUNDER, OBJ_ATTACK, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_EVACT_IGNELETHUNDER)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_EVACT_IGNELETHUNDER)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, 0, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 5000, 0, DAM_TYPE_ELEMENT, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 2500, 0, DAM_TYPE_ELEMENT, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 7500, 0, DAM_TYPE_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 5782
    m_Name = '雷电碎片'
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
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

