# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/talent/p2603.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/talent/p2603.pyc
# Source Generated with Decompyle++
# File: p2603.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_SUBMSG_THROW
from cl_newformula import Func361, Func410, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NeedEnergy', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NotCostNum', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LockNum', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33808, 0, {
        'AddAtt': 300 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33825, 0, {
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'NotCostNum' })) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NeedEnergy', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NotCostNum', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LockNum', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33808, 0, {
        'AddAtt': 450 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33825, 0, {
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'NotCostNum' })) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NeedEnergy', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'NotCostNum', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'LockNum', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 4, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33808, 0, {
        'AddAtt': 600 }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33825, 0, {
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'NotCostNum' })) }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1434: 1 }, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p3703', 0) == 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 33825 }))) > 0:
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33825, -1, 0)
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p3703', 1, 0)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33808, 1, 600)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Source', cl_evact.EventGetTargeID(oWarrior, oEventCB))
            cl_evact.EventCBLionLockStateSearchEnemy(oWarrior, oEventCB, 20, 1, (lambda *a: Func717(*a, **{
'sArg': 'LockNum' })), 0, 0, 1, {
                cl_evact.EventGetTargeID(oWarrior, oEventCB): 1 }, 0)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8018, 0, {
                'Source': (lambda *a: Func361(*a, **{
'sid': 3703,
'sArgs': 'Source' })) }, None)
        elif oWarrior.Energy() >= 6000:
            cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NeedEnergy'), 0)
            cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'p3703', 1, 0)
            cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33808, 1, 600)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Source', cl_evact.EventGetTargeID(oWarrior, oEventCB))
            cl_evact.EventCBLionLockStateSearchEnemy(oWarrior, oEventCB, 20, 1, (lambda *a: Func717(*a, **{
'sArg': 'LockNum' })), 0, 0, 1, {
                cl_evact.EventGetTargeID(oWarrior, oEventCB): 1 }, 0)
            cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 8018, 0, {
                'Source': (lambda *a: Func361(*a, **{
'sid': 3703,
'sArgs': 'Source' })) }, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1439, 1, 0):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33825, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'NotCostNum'), 0)


class CPerform(CCustomPerform):
    m_SID = 2603
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 121

