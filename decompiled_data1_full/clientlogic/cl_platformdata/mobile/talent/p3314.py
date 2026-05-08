# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p3314.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p3314.pyc
# Source Generated with Decompyle++
# File: p3314.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_HANDGUN, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_VICTIM
from cl_newformula import Func444, Func717, Func823

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubColdTime', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransformRatio', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33893, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonEnablePerform(oWarrior, oLifeCycle, 8507)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 1300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubColdTime', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransformRatio', 15)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33893, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonEnablePerform(oWarrior, oLifeCycle, 8507)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CycleTime', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SubColdTime', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'TransformRatio', 20)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33893, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonEnablePerform(oWarrior, oLifeCycle, 8507)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 8507, 'ColdTime', cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'))
    cl_action.CommonPerformSetColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 8507, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CycleTime'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponTypeInPointType(oWarrior, oEventCB, {
        EQUIP_TYPE_FUNDAMENTALWEAPON: 1,
        EQUIP_HANDGUN: 1 }):
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9213, 1, 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func823(*a, **{
'sAttr': 'hittime' }))) == 1 or cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'IsSubColdTime9213', 0) == 0:
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'IsSubColdTime9213', 1, 0)
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 8507, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SubColdTime'), 0)
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'IsSubColdTime', 0) == 0:
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'IsSubColdTime', 1, 0)
            cl_action.CommonSubPointPerformColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 8507, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'SubColdTime'), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0):
        cl_evact.EventCBAddSavedData(oWarrior, oEventCB, '217StoreDamage', (lambda *a: Func444(*a) * Func717(*a, **{
'sArg': 'TransformRatio' }) // 100), 1)
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33893, { }, 0, 0)
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0) and cl_evcon.CheckPerformCodeTime(oWarrior, oEventCB, 8507) == 0:
            cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
            if cl_evcon.EventCBCheckTargetIsLive(oWarrior, oEventCB):
                cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
                cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8507, 0, { }, None)


class CPerform(CCustomPerform):
    m_SID = 3314
    m_Name = '蓄能弹夹'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 114

