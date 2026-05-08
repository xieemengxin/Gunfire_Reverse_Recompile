# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5428.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5428.pyc
# Source Generated with Decompyle++
# File: p5428.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_HANDGUN, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_VICTIM, WARRIOR_MECH, WARRIOR_MONSTER
from cl_newformula import Func308, Func369, Func620, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12039)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit1', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit2', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes1', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes2', 4)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12039)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit1', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit2', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes1', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes2', 5)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12039)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 10, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit1', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit2', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LuckyLimit2', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes1', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes2', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BounceTimes2', 9)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None) and cl_evcon.CheckEventWeaponTypeInPointType(oWarrior, oEventCB, {
        EQUIP_TYPE_FUNDAMENTALWEAPON: 0,
        EQUIP_HANDGUN: 0 }):
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p3915', 1, 0)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func308(*a))) < 3:
            cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, (lambda *a: Func308(*a) * 20))
        elif not cl_evcon.CheckHasState(oWarrior, oEventCB, 32769):
            cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 60)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32769, 300, { }, 1, 0, 0)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p3915', 0):
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit3') and cl_evcon.GetTriggerLuckyHit(oWarrior, oEventCB) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit3'):
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'BounceTimes', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BounceTimes3'))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 1, 0, 0)
            cl_evact.EventCBRemoveFromTargetList(oWarrior, oEventCB, (lambda *a: Func620(*a)))
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                    'Source': (lambda *a: Func620(*a)),
                    'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                    'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                    'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })
            else:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MECH, 0, 0, 0, 0, 1, 0, 0)
                if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                        'Source': (lambda *a: Func620(*a)),
                        'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                        'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                        'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })
        elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit2'):
            pass
        if cl_evcon.GetTriggerLuckyHit(oWarrior, oEventCB) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit2'):
            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'BounceTimes', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BounceTimes2'))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 1, 0, 0)
            cl_evact.EventCBRemoveFromTargetList(oWarrior, oEventCB, (lambda *a: Func620(*a)))
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                    'Source': (lambda *a: Func620(*a)),
                    'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                    'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                    'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })
            else:
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MECH, 0, 0, 0, 0, 1, 0, 0)
                if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                    cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                        'Source': (lambda *a: Func620(*a)),
                        'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                        'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                        'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })
                elif oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit1') and cl_evcon.GetTriggerLuckyHit(oWarrior, oEventCB) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('LuckyLimit1'):
                    cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'BounceTimes', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'BounceTimes1'))
                    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                    cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 0, 0, 0, 0, 1, 0, 0)
                    cl_evact.EventCBRemoveFromTargetList(oWarrior, oEventCB, (lambda *a: Func620(*a)))
                    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                        cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                        cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                            'Source': (lambda *a: Func620(*a)),
                            'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                            'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                            'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })
                    else:
                        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MECH, 0, 0, 0, 0, 1, 0, 0)
                        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                            cl_action.PassiveSetSelfArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Target', cl_evact.EventGetTargeID(oWarrior, oEventCB))
                            cl_evact.EventCBStartClientSkill(oWarrior, oEventCB, 12039, '', 0, 1, {
                                'Source': (lambda *a: Func620(*a)),
                                'Target': (lambda *a: Func717(*a, **{
'sArg': 'Target' })),
                                'Att': (lambda *a: Func369(*a) * Func717(*a, **{
'sArg': 'AttRatio' }) / 10000),
                                'BounceTimes': (lambda *a: Func717(*a, **{
'sArg': 'BounceTimes' })) })


class CPerform(CCustomPerform):
    m_SID = 5428
    m_Name = '锦上添花'
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
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 114

