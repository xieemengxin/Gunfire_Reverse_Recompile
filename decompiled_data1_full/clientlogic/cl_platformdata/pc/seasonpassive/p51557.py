# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51557.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51557.pyc
# Source Generated with Decompyle++
# File: p51557.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_SUBMSG_COMMON, PF_TYPE_THROW
from cl_newformula import Func332, Func369, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1998)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDam', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 500)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', 60)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 100)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1998, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1998)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1998)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 300)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDam', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 1000)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', 60)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 100)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1998, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1998)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1998)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 450)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDam', 80)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 1500)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', 60)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 200)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1998, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1998)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1998)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDam', 120)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 2000)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', 60)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 200)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraRadius', 25)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDamRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1998, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1998)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1998)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'BaseDam', 900)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDam', 180)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AIDamFactor', 2500)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'IntervalTime', 60)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'BaseRadius', 200)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'ExtraTriggerTime', 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraRadius', 50)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraDamRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 10)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 1998, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 1998)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 1):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PF51557_DamCnt', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF1998Cnt') < 5 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PF51557_DamCnt') >= 5:
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PF51557_DamCnt', -5)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1998, 1, {
                'Att': (lambda *a: Func717(*a, **{
'sArg': 'Att' })),
                'ExtraRadius': (lambda *a: Func717(*a, **{
'sArg': 'ExtraRadius' })),
                'ExtraDamRatio': (lambda *a: Func717(*a, **{
'sArg': 'ExtraDamRatio' })),
                'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })),
                'TriggerFinalDam': (lambda *a: Func369(*a)),
                'AIDamFactor': (lambda *a: Func717(*a, **{
'sArg': 'AIDamFactor' })) })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 1):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PF1998Cnt', -1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Att', (lambda *a: Func717(*a, **{
'sArg': 'BaseDam' }) + Func332(*a) * Func717(*a, **{
'sArg': 'ExtraDam' })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 1):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'PF1998Cnt', 1)


class CPerform(CCustomPerform):
    m_SID = 51557
    m_Name = '#NT#绽放'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

