# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25874.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25874.pyc
# Source Generated with Decompyle++
# File: p25874.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO, WARRIOR_NORMAL
from cl_newformula import Func201, Func304, Func361, Func387, Func589

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 11, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 12, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.QueryAttr('ShieldMax') or oWarrior.QueryAttr('ArmorMax'):
        if oWarrior.QueryAttr('ShieldMax'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))
            cl_action.CommonChageMulAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Add' }) * 10000 // Func304(*a, **{
'sAttr': 'ShieldMax' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 1, None)
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'Armor' })))
            cl_action.CommonChageMulAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Add' }) * 10000 // Func304(*a, **{
'sAttr': 'ArmorMax' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 1, None)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))
        cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 1, None)


def DoCallBackAction10(oEventCB, oWarrior):
    cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 25874, 3, None, None)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Ratio', (lambda *a: Func387(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Normal' })))
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Ratio', (lambda *a: Func387(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Plus' })))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Add', (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000))


def DoCallBackAction11(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 25874, 3, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Ratio', (lambda *a: Func387(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Normal' })))
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Ratio', (lambda *a: Func387(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Plus' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Add', (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000))
        if oWarrior.QueryAttr('ShieldMax') or oWarrior.QueryAttr('ArmorMax'):
            if oWarrior.QueryAttr('ShieldMax'):
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'Shield' })))
                cl_action.CommonChageMulAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Add' }) * 10000 // Func304(*a, **{
'sAttr': 'ShieldMax' })))
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 1, None)
            else:
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'Armor' })))
                cl_action.CommonChageMulAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ArmorMax', (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Add' }) * 10000 // Func304(*a, **{
'sAttr': 'ArmorMax' })))
                cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD | DAM_USE_ARMOR, 1, 1, None)
        else:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Before', (lambda *a: Func304(*a, **{
'sAttr': 'HP' })))
            cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'HPMax', 0, (lambda *a: Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' })))
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Sub', (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Before' })))
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func589(*a) * Func361(*a, **{
'sid': 25874,
'sArgs': '25874Ratio' }) // 10000 - Func361(*a, **{
'sid': 25874,
'sArgs': '25874Sub' })), CURE_TYPE_PERFORM | DAM_USE_HP, 1, 1, None)


def DoCallBackAction12(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Normal', (lambda *a: 25 * min(int(Func201(*a)), 4)))
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25874Plus', (lambda *a: 10 * min(int(Func201(*a)), 4)))


class CPerform(CCustomPerform):
    m_SID = 25874
    m_Name = '顺手牵羊'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        10: DoCallBackAction10,
        11: DoCallBackAction11,
        12: DoCallBackAction12 }
    m_BaseArgData = {
        '25874Normal': 100,
        '25874Plus': 100 }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5874
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

