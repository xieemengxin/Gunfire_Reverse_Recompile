# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3803.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3803.pyc
# Source Generated with Decompyle++
# File: p3803.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CREATE_PLANT, OBJ_VICTIM, WARRIOR_PLANT
from cl_newformula import Func308

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33726, 0, {
        'StatusEffect': (lambda *a: 10000 + (Func308(*a) - 1) * 15000) }, 0, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamFromTargetFightType(oWarrior, oEventCB, WARRIOR_PLANT):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33725, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33725, 0, {
                'OneAdd': 300,
                'MaxAdd': 6000 }, 0, 0, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamFromTargetFightType(oWarrior, oEventCB, WARRIOR_PLANT):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33725, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33725, 0, {
                'OneAdd': 400,
                'MaxAdd': 10000 }, 0, 0, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckDamFromTargetFightType(oWarrior, oEventCB, WARRIOR_PLANT):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33725, 0, 1, 0):
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33725, 0, {
                'OneAdd': 500,
                'MaxAdd': 15000 }, 0, 0, 0)
            cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 33725, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 3803
    m_Name = '生意盎然'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 119

