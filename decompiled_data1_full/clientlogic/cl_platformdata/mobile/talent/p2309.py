# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2309.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2309.pyc
# Source Generated with Decompyle++
# File: p2309.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_HANDGUN, MAIN_HOLD, OBJ_SELF
from cl_newformula import Func512

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, None):
        if cl_evcon.GetWeaponCrazyEff(oWarrior, oEventCB) < 40000:
            if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN):
                cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                    1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 10) }, None)
            else:
                cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                    1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 40) }, None)
        else:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) * 0.1 + 3000) }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32260):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32260, 100, { }, 0, 0, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1413, 0, {
            'ThrowMsg': 1 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetWeaponCrazyEff(oWarrior, oEventCB) < 40000:
        if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN):
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 10) }, None)
        else:
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 40) }, None)
    else:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) * 0.1 + 3000) }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckWeaponTypeByHoldType(oWarrior, oEventCB, MAIN_HOLD, EQUIP_HANDGUN):
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 10) }, None)
    else:
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            1: (lambda *a: Func512(*a, **{
'sAttr': 'CrazyEff' }) / 40) }, None)


class CPerform(CCustomPerform):
    m_SID = 2309
    m_Name = '虚空电至'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 104

