# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p6794.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p6794.pyc
# Source Generated with Decompyle++
# File: p6794.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, WARRIOR_ELIDART, WARRIOR_ELIFOOT, WARRIOR_ELIHEVFAR, WARRIOR_ELIHEVNEAR, WARRIOR_ELIMAGIC, WARRIOR_ELIMEDNEAR, WARRIOR_ELISMANEAR, WARRIOR_ELISNIPE, WARRIOR_ELITHROW, WARRIOR_NORBADGER, WARRIOR_NORDART, WARRIOR_NORFOOT, WARRIOR_NORHEVFAR, WARRIOR_NORHEVNEAR, WARRIOR_NORMAGIC, WARRIOR_NORMEDFAR, WARRIOR_NORMEDNEAR, WARRIOR_NORSMAFAR, WARRIOR_NORSMANEAR, WARRIOR_NORSNIPE, WARRIOR_NORTHROW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8037, 0, { }, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8033, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8034, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8035, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8036, 0, { }, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventSetSkillHitInfo(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetSkillHitInfo(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 8032, 0, { }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBADGER) == 0 and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8033, 1, -1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBADGER) == 0 and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8036, 1, -1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIHEVNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIMEDNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELISMANEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORHEVNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMEDNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSMANEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORFOOT) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIFOOT) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORHEVFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIHEVFAR):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8034, 1, -1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if (cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSNIPE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELISNIPE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAGIC) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIMAGIC) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMEDFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSMAFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIDART) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITHROW) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORDART) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORTHROW)) and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8035, 1, -1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8032, 0, 0, None):
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBADGER) == 0 and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8033, 1, -1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORBADGER) == 0 and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8036, 1, -1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIHEVNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIMEDNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELISMANEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORHEVNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMEDNEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSMANEAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORFOOT) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIFOOT) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORHEVFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIHEVFAR):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8034, 1, -1)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if (cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSNIPE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELISNIPE) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAGIC) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIMAGIC) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMEDFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORSMAFAR) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELIDART) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITHROW) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORDART) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORTHROW)) and cl_evcon.CheckTargetPointBaseMonster(oWarrior, oEventCB, 2321) == 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 8035, 1, -1)


class CPerform(CCustomPerform):
    m_SID = 6794
    m_Name = '一击击杀'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

