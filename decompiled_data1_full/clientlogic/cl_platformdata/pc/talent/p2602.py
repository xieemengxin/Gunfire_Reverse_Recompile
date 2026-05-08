# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2602.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2602.pyc
# Source Generated with Decompyle++
# File: p2602.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func443, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1979)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionRadius', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionTimes', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateRatio', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 6, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1979)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionRadius', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 150)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionTimes', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateRatio', 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 6, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1979)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 3, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionRadius', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExplosionTimes', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddStateRatio', 30)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckDamIsExplosion(oWarrior, oEventCB) and cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9793: 1,
        9792: 1,
        9709: 1,
        9794: 1,
        9791: 1,
        9703: 1,
        9799: 1,
        9704: 1,
        9701: 1,
        9705: 1,
        9706: 1,
        9707: 1 }, 1, 0) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBSetTransInfo(oWarrior, oEventCB, 'AddExplosionNum', 1)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8155, 0, 1, 0) and cl_evcon.EventCBGetTargetStateReasonData(oWarrior, oEventCB, 8155, 'ActNum', 1) != cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func443(*a))):
            cl_evact.EventCBAddTargetStateStatistics(oWarrior, oEventCB, 8155, 'ExplosionNum', cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'AddExplosionNum', 1), 1)
            if cl_evcon.EventCBCheckTargetStateStatistics(oWarrior, oEventCB, 8155, 'ExplosionNum', 1, 0) >= 4:
                cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 8155, 0, 0, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if (cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8155) or cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8156)) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TransFlag') == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 1979, {
            'VID': cl_evact.EventGetTargeID(oWarrior, oEventCB) }, {
            'ExplosionRadius': (lambda *a: Func717(*a, **{
'sArg': 'ExplosionRadius' })),
            'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })),
            'ExplosionTimes': (lambda *a: Func717(*a, **{
'sArg': 'ExplosionTimes' })),
            'AddStateRatio': (lambda *a: Func717(*a, **{
'sArg': 'AddStateRatio' })) }, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20031):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBSetTransInfo(oWarrior, oEventCB, 'AddExplosionNum', 2)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8155, 0, 1, 0) and cl_evcon.EventCBGetTargetStateReasonData(oWarrior, oEventCB, 8155, 'ActNum', 1) != cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func443(*a))):
            cl_evact.EventCBAddTargetStateStatistics(oWarrior, oEventCB, 8155, 'ExplosionNum', cl_evcon.EventCBGetTransInfo(oWarrior, oEventCB, 'AddExplosionNum', 1), 1)
            if cl_evcon.EventCBCheckTargetStateStatistics(oWarrior, oEventCB, 8155, 'ExplosionNum', 1, 0) >= 4:
                cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 8155, 0, 0, 1)


class CPerform(CCustomPerform):
    m_SID = 2602
    m_Name = '#NT#觉醒占位'
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
        3: DoCallBackAction3,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 121

