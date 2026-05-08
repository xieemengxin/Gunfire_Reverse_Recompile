# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51366.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51366.pyc
# Source Generated with Decompyle++
# File: p51366.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, PF_SUBMSG_THROW
from cl_newformula import Func343, Func360, Func651, Func717, Func722

def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11135, 2)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11135, 3)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerCnt', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11135, 4)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerRatio', 45)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TriggerCnt', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11135, 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 215):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 21, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 8007)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 217):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 22, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 8009)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 212):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 23, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 8013)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 8012)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1413)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 8014)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 12008)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214):
        cl_action.CommonAddPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1430)
    if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, 8, 0, 0)
    if not cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 205) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12030, 0, 0) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('12030Trigger'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '12030Trigger', 0)
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 0, 1, 0)
    elif not cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219):
        if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            1439: 1 }, 0, 0):
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'TrueCnt', (lambda *a: min(int(Func343(*a, **{
'sid': 4508 }) - Func360(*a, **{
'sid': Func722(*a),
'sAttr': 'TriggerTimes' })), int(Func717(*a, **{
'sArg': 'TriggerCnt' })))))
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TrueCnt') > 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func717(*a, **{
'sArg': 'TriggerRatio' }))):
                cl_evact.PassiveExtBulletUse(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })))
                cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: -Func717(*a, **{
'sArg': 'DamRatio' })), 0, 1, 0)
                cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'P51366', 1, 0)
                if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
                    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33822, 0, {
                        'Count': (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })),
                        'Damage': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 0, 0)
                elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 220):
                    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33820, 0, {
                        'Count': (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })),
                        'Damage': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 0, 0)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 13556, 0, 0):
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 12030, 'TriggerTimes', 0, 0)
        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'TrueCnt', (lambda *a: min(int(Func343(*a, **{
'sid': 4508 })), int(Func717(*a, **{
'sArg': 'TriggerCnt' })))))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TrueCnt') > 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: Func717(*a, **{
'sArg': 'TriggerRatio' }))):
            cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 4508, (lambda *a: -Func717(*a, **{
'sArg': 'TrueCnt' })), 0)
            cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 12030, 'TriggerTimes', 0, (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '12030Trigger', 1)
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '12030Trigger', 0)


def DoCallBackAction21(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P51366', 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33821, 0, {
            'TargetPos': cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'Start'),
            'Count': (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })),
            'Damage': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 0, 0)


def DoCallBackAction22(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P51366', 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RayActive' }))) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33821, 0, {
            'TargetPos': cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'Start'),
            'Count': (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })),
            'Damage': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 0, 0)


def DoCallBackAction23(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P51366', 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33821, 0, {
            'TargetPos': cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'Start'),
            'Count': (lambda *a: Func717(*a, **{
'sArg': 'TrueCnt' })),
            'Damage': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51366
    m_Name = '灵力风暴'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        8: DoCallBackAction8,
        21: DoCallBackAction21,
        22: DoCallBackAction22,
        23: DoCallBackAction23 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

