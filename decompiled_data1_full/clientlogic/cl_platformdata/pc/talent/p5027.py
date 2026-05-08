# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5027.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5027.pyc
# Source Generated with Decompyle++
# File: p5027.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJECT_SERVANT, OBJ_ATTACK, OBJ_VICTIM, TAG_RESCUE_MECHREMOTE
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCD', 6000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 3)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33956, 0, { }, 1)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33956, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 51230, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33955, 0, 0, 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 20000, 0, DAM_TYPE_WEAPON, '')
        cl_evact.EventCBChangeLuckyHit(oWarrior, oEventCB, 100)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB):
        cl_evact.EventCBSubSelfColdTime(oWarrior, oEventCB, 100)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0) and cl_evcon.CheckRescueTag(oWarrior, oEventCB, TAG_RESCUE_MECHREMOTE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckTargetFormSelfByType(oWarrior, oEventCB, OBJECT_SERVANT):
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33956, 0)
            cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'AddCD' })))
            cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
            cl_evact.EventCBTarget2ListenerUsePerform(oWarrior, oEventCB, 1997, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBTargetRemovePerform(oWarrior, oEventCB, 51230)


class CPerform(CCustomPerform):
    m_SID = 5027
    m_Name = '步坦协同'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 3
    m_IsRareTalent = 1
    m_Career = 114

