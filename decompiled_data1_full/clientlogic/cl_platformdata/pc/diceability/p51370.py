# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51370.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51370.pyc
# Source Generated with Decompyle++
# File: p51370.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COMMONACTIVE_TAG_SEASONDICE, DAM_MASK_ELEMENT, DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, OBJ_ATTACK, PF_SUBMSG_COMMON
from cl_newformula import Func651, Func663, Func817

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 10)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 2, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddDam', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 2, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseTriggerRatio', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'S6DiceSkill', 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddDam'), 0, DAM_MASK_ELEMENT, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TriggerRatio')) and cl_evcon.EventCBCheckPerfromInActivePerformTag(oWarrior, oEventCB, COMMONACTIVE_TAG_SEASONDICE) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, '51370ExtraTrigger') == 0:
        cl_evact.EventCBCopySkillCustom(oWarrior, oEventCB, {
            'IgnoreLayer': 1 })
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, (lambda *a: Func663(*a)), { }, {
            '51370ExtraTrigger': 1 }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TriggerRatio')) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        51336: 1,
        51338: 1 }, 1, 0):
        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TriggerPerformID' })), '', 0, 1, {
            'DiceID': (lambda *a: Func651(*a, **{
'sKey': 'Item' })) })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseTriggerRatio') * Func817(*a))) and cl_evcon.EventCBCheckPerfromInActivePerformTag(oWarrior, oEventCB, COMMONACTIVE_TAG_SEASONDICE) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, '51370ExtraTrigger') == 0:
        cl_evact.EventCBCopySkillCustom(oWarrior, oEventCB, {
            'IgnoreLayer': 1 })
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, (lambda *a: Func663(*a)), { }, {
            '51370ExtraTrigger': 1 }, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseTriggerRatio') * Func817(*a))) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        51336: 1,
        51338: 1 }, 1, 0):
        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TriggerPerformID' })), '', 0, 1, {
            'DiceID': (lambda *a: Func651(*a, **{
'sKey': 'Item' })) })


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'S6DiceSkill', 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BaseDam') * Func817(*a)), 0, DAM_MASK_ELEMENT, '')


class CPerform(CCustomPerform):
    m_SID = 51370
    m_Name = '骰力增幅'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

