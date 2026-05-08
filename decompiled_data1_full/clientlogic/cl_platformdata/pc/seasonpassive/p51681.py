# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51681.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51681.pyc
# Source Generated with Decompyle++
# File: p51681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, PF_SUBMSG_COMMON, S7MODULE_TAG_BLOOM, S7_ALL_PERFORM_ENABLE, WARRIOR_MONSTER
from cl_newformula import Func369, Func555, Func604, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2008)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 9, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 2008, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 2008)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2008)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 9, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 2008, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 2008)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2008)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 9, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 2008, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 2008)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 2008)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_COMMON, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 9, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    if cl_condition.GetUsingSkillNumBySID(oWarrior, oLifeCycle, 2008, 1) >= 1:
        cl_action.CommonHaltPointPerform(oWarrior, oLifeCycle, 2008)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'TriggerEle') != 0:
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'TriggerEle', 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'DetectRange' })), WARRIOR_MONSTER, 1, 0, (lambda *a: Func859(*a, **{
'sAttr': 'TargetNum' })), 0, 1, 0, 0, 1)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('P51681Cnt') < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'MaxCnt' }))):
                cl_evact.EventCBUsePerform(oWarrior, oEventCB, 2008, 0, {
                    'Att': (lambda *a: Func369(*a) * Func859(*a, **{
'sAttr': 'DamRatio' }) / 100),
                    'Radius': (lambda *a: Func604(*a, **{
'sKey': 'CurRadius' })) })


def DoCallBackAction2(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('P51681Cnt') < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'MaxCnt' }))):
        cl_evact.EventCBUsePerform(oWarrior, oEventCB, 2008, 0, {
            'Att': (lambda *a: Func369(*a) * Func859(*a, **{
'sAttr': 'DamRatio' }) / 100),
            'Radius': (lambda *a: Func604(*a, **{
'sKey': 'CurRadius' })) })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.EventCBGetEquipS7ModuleNum(oWarrior, oEventCB, 2017, S7MODULE_TAG_BLOOM, 0, 0, 0, 1):
        cl_action.CommonSetPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1998, 'DebuffProb', (lambda *a: Func717(*a, **{
'sArg': 'DebuffProb' })))
        cl_action.CommonChangePerformDamType(oWarrior, oEventCB.GetCBLifeCycle(), 1998, (lambda *a: Func555(*a, **{
'sAttr': 'ElementType' })))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonChangePerformDamType(oWarrior, oEventCB.GetCBLifeCycle(), 1998, (lambda *a: Func555(*a, **{
'sAttr': 'ElementType' })))


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 0):
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', (lambda *a: Func859(*a, **{
'sAttr': 'PerDebuffProb' })), 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 2008, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'P51681Cnt', -1)


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 2008, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'P51681Cnt', 1)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 0):
        cl_evact.EventCBSetSkillCustomInfo(oWarrior, oEventCB, 'TriggerEle', 1)


class CPerform(CCustomPerform):
    m_SID = 51681
    m_Name = '莲花-元素莲花'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9 }
    m_BaseArgData = {
        'DebuffProb': 3000 }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'DetectRange': 8,
            'TargetNum': 1,
            'DamRatio': 10,
            'MaxCnt': 3 },
        2: {
            'DetectRange': 10,
            'TargetNum': 1,
            'DamRatio': 20,
            'MaxCnt': 3 },
        3: {
            'DetectRange': 12,
            'TargetNum': 2,
            'DamRatio': 20,
            'PerDebuffProb': 150,
            'MaxCnt': 3 },
        4: {
            'DetectRange': 14,
            'TargetNum': 3,
            'DamRatio': 20,
            'PerDebuffProb': 200,
            'MaxCnt': 3 } }

