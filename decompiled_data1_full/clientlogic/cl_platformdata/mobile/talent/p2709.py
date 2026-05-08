# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2709.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2709.pyc
# Source Generated with Decompyle++
# File: p2709.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func509

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None):
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 0, 2, 0, 1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 3)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None):
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 3, 0, 1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None):
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 4, 0, 1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 6)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '1383', None) == 0:
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32500, 600, { }, 0, 0, None)
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '1383', 4, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '1383', None) == 0:
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32500, 600, { }, 0, 0, None)
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '1383', 4, None)
        if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)
        else:
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '1383', None) == 0:
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 32500, 0, 1, None) == 0:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32500, 600, { }, 0, 0, None)
        cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '1383', 4, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func509(*a, **{
'sAttr': 'Att' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 0, 0, None, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 2709
    m_Name = '花开烂漫'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 109

