# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51349.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51349.pyc
# Source Generated with Decompyle++
# File: p51349.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, DPSUBMSG_DEFAULT
from cl_newformula import Func303

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33798, 0, {
        'ReplyScale': 1,
        'ReplyValue': 15,
        'StatusEffect': 500,
        'ElementScale': 100 }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33798, 0, {
        'ReplyScale': 2,
        'ReplyValue': 10,
        'StatusEffect': 500,
        'ElementScale': 100 }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33798, 0, {
        'ReplyScale': 3,
        'ReplyValue': 7,
        'StatusEffect': 500,
        'ElementScale': 100 }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33798, 0, {
        'ReplyScale': 4,
        'ReplyValue': 5,
        'StatusEffect': 500,
        'ElementScale': 100 }, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33798, 0, {
        'ReplyScale': 5,
        'ReplyValue': 5,
        'StatusEffect': 500,
        'ElementScale': 100 }, 1)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        2: 3333,
        3: 3334 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'ExtEleAbnormal', 1024)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'ExtEleAbnormal', 512)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'ExtEleAbnormal', 256)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'ExtEleAbnormal' })), 10000, 0)


class CPerform(CCustomPerform):
    m_SID = 51349
    m_Name = '元素弹匣'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

