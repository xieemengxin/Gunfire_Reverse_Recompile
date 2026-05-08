# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25714.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25714.pyc
# Source Generated with Decompyle++
# File: p25714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DAM_USE_HP, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_LOW, WARRIOR_ELITE, WARRIOR_HERO, WARRIOR_SERVANT
from cl_newformula import Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
            if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
            else:
                cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 10 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
        else:
            cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 10 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
            cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0 and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 3):
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_SERVANT) or cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
            cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
                3: 3333,
                4: 3333,
                5: 3334 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, 10000, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, 10000, None)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, 10000, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 2 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
    else:
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 10 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, 0, -1, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


class CPerform(CCustomPerform):
    m_SID = 25714
    m_Name = '元素馈赠'
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
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5714
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

