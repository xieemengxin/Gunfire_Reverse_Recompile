# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4027.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4027.pyc
# Source Generated with Decompyle++
# File: p4027.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_FRIEND_HERO, OBJ_VICTIM, SCENE_EVT_SHAPE_SPHERE
from cl_newformula import Func331

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1410, 0, None):
        cl_evact.PassiveSetPosToCartoon(oWarrior, oEventCB)
        cl_evact.PassiveCBAddSceneEvent(oWarrior, oEventCB, 500, SCENE_EVT_SHAPE_SPHERE, {
            'Radius': 5 }, 0, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_FRIEND_HERO) == 0:
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2118):
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 10000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, None, None)
        elif cl_evcon.CheckTalent(oWarrior, oEventCB, 2118) == 0 and cl_evcon.CheckTalent(oWarrior, oEventCB, 2117):
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 20000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, None, None)
        else:
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 80000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2114):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32106, 500, {
                'TalentAffection': 0 }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2115):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32107, 500, {
                'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2115 }) * -2000 + -2000) }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2116):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32108, 500, {
                'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2116 }) * 2500 + 2500) }, 0, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetSideType(oWarrior, oEventCB, OBJ_FRIEND_HERO) == 0:
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2118):
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 10000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, None, None)
        elif cl_evcon.CheckTalent(oWarrior, oEventCB, 2118) == 0 and cl_evcon.CheckTalent(oWarrior, oEventCB, 2117):
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 20000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, None, None)
        else:
            cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 80000)
            cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2114):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32106, 500, {
                'TalentAffection': 0 }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2115):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32107, 500, {
                'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2115 }) * -2000 + -2000) }, 0, None, None)
        if cl_evcon.CheckTalent(oWarrior, oEventCB, 2116):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32108, 500, {
                'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2116 }) * 2500 + 2500) }, 0, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckTalent(oWarrior, oEventCB, 2118):
        cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 10000)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20028, 500, { }, 0, None, None)
    elif cl_evcon.CheckTalent(oWarrior, oEventCB, 2118) == 0 and cl_evcon.CheckTalent(oWarrior, oEventCB, 2117):
        cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 20000)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, None, None)
    else:
        cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 80000)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, None, None)
    if cl_evcon.CheckTalent(oWarrior, oEventCB, 2114):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32106, 500, {
            'TalentAffection': 0 }, 0, None, None)
    if cl_evcon.CheckTalent(oWarrior, oEventCB, 2115):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32107, 500, {
            'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2115 }) * -2000 + -2000) }, 0, None, None)
    if cl_evcon.CheckTalent(oWarrior, oEventCB, 2116):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32108, 500, {
            'TalentAffection': (lambda *a: Func331(*a, **{
'sid': 2116 }) * 2500 + 2500) }, 0, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckTalent(oWarrior, oEventCB, 2118) == 0 and cl_evcon.CheckTalent(oWarrior, oEventCB, 2117):
        cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 20000)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20026, 500, { }, 0, None, None)
    else:
        cl_evact.PassiveAddCustomDamage(oWarrior, oEventCB, 80000)
        cl_evact.PassiveAddTargetStateWithCache(oWarrior, oEventCB, 20027, 500, { }, 0, None, None)


class CPerform(CCustomPerform):
    m_SID = 4027
    m_Name = '1410烟雾手雷被动技能（待废弃）'
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
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0

