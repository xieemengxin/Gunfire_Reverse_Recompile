# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51593.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51593.pyc
# Source Generated with Decompyle++
# File: p51593.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func354, Func610, Func717, Func746
from cl_commondefines import ATTACKERSUBMSG_NORMAL, FIGHT_KEY_IGNOREDAMAGE, OBJECT_OWNER, OBJ_VICTIM, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 1000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33948, 0, {
        'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffProp', 1000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 2000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33948, 0, {
        'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffProp', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 3000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StorageRatio', 50)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39723, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33948, 0, {
        'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffProp', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AttRatio', 4000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'StorageRatio', 100)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39723, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33948, 0, {
        'AttRatio': (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' })) }, 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DebuffProp', 6000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1991, 0, 0):
        cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: Func717(*a, **{
'sArg': 'AttRatio' }) * Func746(*a, **{
'iStateSID': 33948 })), 0, 0, 0)
        cl_evact.EventChangeSkillCache(oWarrior, oEventCB, 'DebuffProb', (lambda *a: Func717(*a, **{
'sArg': 'DebuffProp' })), 0)
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33948, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1991, 0, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Phase', 0) == 1:
        cl_evact.EventCBAddStateStatistics(oWarrior, oEventCB, (lambda *a: Func354(*a) * Func717(*a, **{
'sArg': 'StorageRatio' }) // 10000), 39723, 'StorageDam')
        cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'st39723', (lambda *a: Func610(*a, **{
'iStateSID': 39723,
'sKey': 'StorageDam' })), 1)
        cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func610(*a, **{
'iStateSID': 39723,
'sKey': 'StorageDam' })) }, 39723)
        if cl_condition.GetStateStatistics(oWarrior, oEventCB.GetCBLifeCycle(), 39723, 'StorageDam') >= 500 and cl_action.PassiveGetLiteCDRemainTime(oWarrior, oEventCB.GetCBLifeCycle()) == 0:
            cl_evact.EventTargetGetSectorTargetByFightType(oWarrior, oEventCB, WARRIOR_MONSTER, 50, 30, 120, 0, 1, FIGHT_KEY_IGNOREDAMAGE, 0, 1, 1, cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_VICTIM))
            if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)
                cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1995, 1, {
                    'Radius': 2,
                    'Att': (lambda *a: Func610(*a, **{
'iStateSID': 39723,
'sKey': 'StorageDam' }) * 100) }, OBJECT_OWNER)
                cl_action.CommonStateStatistics(oWarrior, oEventCB.GetCBLifeCycle(), 39723, 0, 'StorageDam')
                cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'st39723', (lambda *a: Func610(*a, **{
'iStateSID': 39723,
'sKey': 'StorageDam' })), 1)
                cl_action.CommonRefreshStateExtraInfo(oWarrior, oEventCB.GetCBLifeCycle(), {
                    'ExcessiveDam': (lambda *a: Func610(*a, **{
'iStateSID': 39723,
'sKey': 'StorageDam' })) }, 39723)


class CPerform(CCustomPerform):
    m_SID = 51593
    m_Name = '#NT#双响流星'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

