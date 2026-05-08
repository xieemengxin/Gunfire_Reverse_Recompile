# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51363.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51363.pyc
# Source Generated with Decompyle++
# File: p51363.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import ASSEMBLE_DICE_SUMADD, ASSEMBLE_DICE_SUMSUB, ATTACKERSUBMSG_NORMAL, DICETAG_SEASONOUTPUT, DICE_PUTOUT_POLL_THREE, FIGHT_KEY_IGNOREDAMAGE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, OBJ_SELF, WARRIOR_MONSTER
from cl_newformula import Func410, Func717, Func804, Func821

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33849, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttMul', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttAdd', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxPoint', 0)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33849)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33849, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttMul', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttAdd', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerEnermy', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxPoint', 10)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 500, 500, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMADD, 2, 0)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMSUB, 3, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func821(*a))) >= 45:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33849)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33849, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttMul', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttAdd', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerEnermy', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxPoint', 25)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMADD, 2, 0)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMSUB, 3, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func821(*a))) >= 45:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33849)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 8, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33849, 0, { }, 0)
    cl_action.CommonUpdateStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Cnt', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttMul', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttAdd', 400)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerEnermy', 10)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 0)
    cl_action.CommonAddSelfNeedSubCDPerform(oWarrior, oLifeCycle)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMADD, 2, 0)
    cl_action.CommonListenAssembleDiceSumThreshold(oWarrior, oLifeCycle, 45, ASSEMBLE_DICE_SUMSUB, 3, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxPoint', 25)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func821(*a))) >= 45:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonRemoveStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0)
    if cl_condition.CommonCheckStateArgsDict(oWarrior, oLifeCycle, 33849, 'EffectCount', 0, 0) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33849)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel'):
        cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 30, 30, 120, 0, 1, FIGHT_KEY_IGNOREDAMAGE, 0, 1, 1, None)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) <= 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: max(30, Func717(*a, **{
'sArg': 'AttDis' }))), WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'MaxPoint' }))) > 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: min(Func410(*a, **{
'sid': 33849 }), Func717(*a, **{
'sArg': 'MaxPoint' })) + Func821(*a)))
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'NoMaxPoint' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: Func410(*a, **{
'sid': 33849 }) + Func821(*a)))
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: Func821(*a)))
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1749, {
                'Att': (lambda *a: (Func717(*a, **{
'sArg': 'ExcutePoint' }) * Func717(*a, **{
'sArg': 'AttMul' }) + Func717(*a, **{
'sArg': 'AttAdd' })) * 100),
                'Cnt': (lambda *a: Func717(*a, **{
'sArg': 'Cnt' })) }, 0)
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
                'pfid': 51363,
                'Item': (lambda *a: Func804(*a)),
                'TriggerPerformID': 1749 })
    else:
        cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 50, 30, 120, 0, 1, FIGHT_KEY_IGNOREDAMAGE, 0, 1, 1, None)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) <= 0:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: max(30, Func717(*a, **{
'sArg': 'AttDis' }))), WARRIOR_MONSTER, 1, 0, 1, 0, 1, 0, None)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'MaxPoint' }))) > 0:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: min(Func410(*a, **{
'sid': 33849 }), Func717(*a, **{
'sArg': 'MaxPoint' })) + Func821(*a)))
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'NoMaxPoint' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: Func410(*a, **{
'sid': 33849 }) + Func821(*a)))
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExcutePoint', (lambda *a: Func821(*a)))
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) > 0:
            cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1749, {
                'Att': (lambda *a: (Func717(*a, **{
'sArg': 'ExcutePoint' }) * Func717(*a, **{
'sArg': 'AttMul' }) + Func717(*a, **{
'sArg': 'AttAdd' })) * 100),
                'Cnt': (lambda *a: Func717(*a, **{
'sArg': 'Cnt' })) }, 0)
            cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
                'pfid': 51363,
                'Item': (lambda *a: Func804(*a)),
                'TriggerPerformID': 1749 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckAssistKill(oWarrior, oEventCB):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', 1)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'HitNum' }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TriggerEnermy' }))) and cl_condition.GetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33849) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'MaxPoint' }))):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HitNum', (lambda *a: -Func717(*a, **{
'sArg': 'TriggerEnermy' })))
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33849, 1, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    else:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 30)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsNormalLevel'):
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 50)
    elif cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'InNormalLevel') == 0:
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'IsNormalLevel', 1)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'AttDis', 30)


class CPerform(CCustomPerform):
    m_SID = 51363
    m_Name = '鸿运流星'
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
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        8: DoCallBackAction8,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_SEASONOUTPUT,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_THREE

