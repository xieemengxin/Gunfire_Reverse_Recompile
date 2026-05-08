# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51389.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51389.pyc
# Source Generated with Decompyle++
# File: p51389.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, FIGHT_KEY_WUDI, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func343, Func602, Func804

def Action1(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33885):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 650)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageReduce', -5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33885, { }, 0, 0)


def Action2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33885):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageReduce', -5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33885, { }, 0, 0)


def Action3(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33885):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageReduce', -5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33885, { }, 0, 0)


def Action4(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33885):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 350)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageReduce', -5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33885, { }, 0, 0)


def Action5(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33885):
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33885, 0, { }, 0)
        cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 1, 0, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 250)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 4, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamageReduce', -5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33885, 'EnableCount', 0, 0)
    cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33885, { }, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33885):
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 0, 1, None)
    if cl_evcon.GetTargetNum(oWarrior, oEventCB) > 0:
        if (cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220)) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33604):
            cl_evact.EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, 0, {
                'CardNum': 3,
                'QualityNum': 1,
                'AssignEndPos': {
                    206: 1,
                    207: 1,
                    213: 1,
                    217: 1,
                    218: 1 },
                'CustomData': {
                    217: {
                        'DamMul': 1 } },
                'HalfHeight': {
                    206: 1 },
                'CommonCustomData': {
                    'TriggerOrigin': (lambda *a: Func804(*a)) } })
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
                'pfid': 51389,
                'Item': (lambda *a: Func804(*a)) })
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Count') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func602(*a) * 0.5 + 1)) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))):
                cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 7, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count'))
            else:
                cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1988, { }, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1988: 1 }, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, 0, {
            'CardNum': 3,
            'QualityNum': 1,
            'AssignEndPos': {
                206: 1,
                207: 1,
                213: 1,
                217: 1,
                218: 1 },
            'CustomData': {
                217: {
                    'DamMul': 1 } },
            'HalfHeight': {
                206: 1 },
            'CommonCustomData': {
                'TriggerOrigin': (lambda *a: Func804(*a)) } })
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51389,
            'Item': (lambda *a: Func804(*a)) })
        if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
            cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 8010)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Count') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func602(*a) * 0.5 + 1)) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))):
            cl_evact.RepeatTriggerGroup(oWarrior, oEventCB, 7, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count'))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'IsTrigger', 0) == 0 and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'TriggerOrigin') == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func804(*a))):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'IsTrigger', 1, 0)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'DamageReduce'), 0, 1, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 20, 10, 60, 0, 1, FIGHT_KEY_WUDI, 0, 0, 1, None)
    if cl_evcon.GetTargetNum(oWarrior, oEventCB) > 0:
        cl_evact.EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, 0, {
            'CardNum': 3,
            'QualityNum': 1,
            'AssignEndPos': {
                206: 1,
                207: 1,
                213: 1,
                217: 1,
                218: 1 },
            'CustomData': {
                217: {
                    'DamMul': 1 } },
            'HalfHeight': {
                206: 1 },
            'CommonCustomData': {
                'TriggerOrigin': (lambda *a: Func804(*a)) } })
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 51389,
            'Item': (lambda *a: Func804(*a)) })
        if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
            cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 8010)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 33885):
        cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 51389
    m_Name = '自动施法'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        7: DoCallBackAction7,
        8: DoCallBackAction8 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

