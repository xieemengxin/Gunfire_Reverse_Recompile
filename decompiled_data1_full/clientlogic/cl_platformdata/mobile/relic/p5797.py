# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5797.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5797.pyc
# Source Generated with Decompyle++
# File: p5797.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_ELEMENT, DAM_TYPE_THUNDER, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL, WARRIOR_BUILD
from cl_newformula import Func213

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20028) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BUILD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20028, (lambda *a: Func213(*a) * 100 / 100 + 0), { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20028, 0, None, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 7500, 0, DAM_TYPE_ELEMENT, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20028) and cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_BUILD):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20028, (lambda *a: Func213(*a) * 100 / 100 + 0), { }, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_THUNDER, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 7500, 0, DAM_TYPE_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 5797
    m_Name = '雷电狂热'
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
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

