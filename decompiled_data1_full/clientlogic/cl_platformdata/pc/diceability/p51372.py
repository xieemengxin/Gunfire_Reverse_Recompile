# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51372.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51372.pyc
# Source Generated with Decompyle++
# File: p51372.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_SELF
from cl_newformula import Func304

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33870, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageResAdd', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpNeed', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oLifeCycle, {
        'ExcessiveDam': cl_action.CommonGetStateArgsDictSum(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) }, 33870)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33870)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33870, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageResAdd', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpAddPercent', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpNeed', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oLifeCycle, {
        'ExcessiveDam': cl_action.CommonGetStateArgsDictSum(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) }, 33870)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33870)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33870, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageResAdd', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpAddPercent', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpNeed', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oLifeCycle, {
        'ExcessiveDam': cl_action.CommonGetStateArgsDictSum(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) }, 33870)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33870)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33870, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageResAdd', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpAddPercent', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'HpNeed', 100)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oLifeCycle, {
        'ExcessiveDam': cl_action.CommonGetStateArgsDictSum(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) }, 33870)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33870, 'Effect', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33870)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpAddPercent') / 100), 0 | DAM_USE_HP, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'NowDamageAdd', (lambda *a: (Func304(*a, **{
'sAttr': 'HP' }) / cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HpNeed')) * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamageResAdd')))
    cl_action.CommonChangeBaseDamRatio(oWarrior, oEventCB.GetCBLifeCycle(), 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NowDamageAdd'), 0, 1)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oEventCB.GetCBLifeCycle(), 33870, 'Effect', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NowDamageAdd'), 0, 0)
    cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_action.CommonGetStateArgsDictSum(oWarrior, oEventCB.GetCBLifeCycle(), 33870, 'Effect', 0, 0) }, 33870)


class CPerform(CCustomPerform):
    m_SID = 51372
    m_Name = '血气之勇'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

