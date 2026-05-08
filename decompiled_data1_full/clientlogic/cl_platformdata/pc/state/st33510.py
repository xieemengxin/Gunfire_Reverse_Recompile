# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33510.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33510.pyc
# Source Generated with Decompyle++
# File: st33510.pyc (Python 3.6)

from cl_platformdata.custom.state.customaction import CustomAction33510Add, CustomAction33510Update
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ALL_NOSELF, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404, Func429, Func437, Func745, Func748

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33510, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })), (lambda *a: 600 + 200 * Func429(*a, **{
'sArg': 'TalentLevel' })))
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGEPERFORMCDRATIO, -1, 1)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    CustomAction33510Update(oTarget, oLifeCycle, { })


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBSelfAttackerUsePerformEvtTarget(oTarget, oEventCB, 1973, {
        'Dam': (lambda *a: Func437(*a, **{
'sKey': 'Dam' }) / min(int(max(Func404(*a), 1)), 6)),
        'CopyTimes': (lambda *a: min(int(max(Func404(*a) - 1, 0)), 6)) })


def CallBack1(oEventCB, oTarget):
    cl_action.StateChangeStateDelayInfo(oTarget, oEventCB.GetCBLifeCycle(), 0, (lambda *a: 100 / (1 + Func745(*a, **{
'iType': 2 }) / 10000)), 0)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 5, 0, 0)


def CallBack5(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'TransmitNum'):
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 15121, 0, 100)
        cl_evact.EventGetStateInfoTarget(oTarget, oEventCB)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 40, WARRIOR_MONSTER, 1, 0, (lambda *a: 2 + Func429(*a, **{
'sArg': 'TalentLevel' })), 0, 1, 0, None)
        cl_evact.EventCBRemoveSelfFromTarget(oTarget, oEventCB)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33510Flag', 0)
        if cl_evcon.GetThisTargetNum(oTarget, oEventCB) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: 1 + Func429(*a, **{
'sArg': 'TalentLevel' }))):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33510Copy', (lambda *a: 1 + Func429(*a, **{
'sArg': 'TalentLevel' }) - cl_evcon.GetThisTargetNum(oTarget, oEventCB)))
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33510Flag', 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 13)


def CallBack6(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamReduce'):
        CustomAction33510Add(oTarget, oEventCB.GetCBLifeCycle(), {
            'Transmit': 1,
            'CurDam': (lambda *a: Func429(*a, **{
'sArg': 'Att' })) })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33511, (lambda *a: Func748(*a)), 1, {
            'StateCount': (lambda *a: 20 * Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)
    else:
        CustomAction33510Add(oTarget, oEventCB.GetCBLifeCycle(), {
            'Transmit': 0,
            'CurDam': (lambda *a: Func429(*a, **{
'sArg': 'Att' })) })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33511, (lambda *a: Func748(*a)), 1, {
            'StateCount': (lambda *a: 20 * Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)


def CallBack7(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DamReduce'):
        CustomAction33510Add(oTarget, oEventCB.GetCBLifeCycle(), {
            'Transmit': 1,
            'CurDam': (lambda *a: Func429(*a, **{
'sArg': 'Att' })) })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33511, (lambda *a: Func748(*a)), 1, {
            'StateCount': (lambda *a: 20 * Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)
    else:
        CustomAction33510Add(oTarget, oEventCB.GetCBLifeCycle(), {
            'Transmit': 0,
            'CurDam': (lambda *a: Func429(*a, **{
'sArg': 'Att' })) })
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33511, (lambda *a: Func748(*a)), 1, {
            'StateCount': (lambda *a: 20 * Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 5, 0, 0)


def CallBack13(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33510Flag'):
        cl_evact.StateCBSelfAttackerUsePerformEvtTarget(oTarget, oEventCB, 1733, {
            'TransmitDam': (lambda *a: Func437(*a, **{
'sKey': 'TransmitDam' }) * 10 // 100),
            'AID': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' })),
            'TalentLevel': (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' })),
            'StateCount': 1,
            'ChooseSelf': 1 })
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33510Flag', 1)
        cl_evact.StateCBSelfAttackerUsePerformEvtTarget(oTarget, oEventCB, 1733, {
            'TransmitDam': (lambda *a: (Func437(*a, **{
'sKey': 'TransmitDam' }) * 10 // 100) * (Func437(*a, **{
'sKey': '33510Copy' }) + 1)),
            'AID': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' })),
            'TalentLevel': (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' })),
            'StateCount': (lambda *a: Func437(*a, **{
'sKey': '33510Copy' }) + 1),
            'ChooseSelf': 1 })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 6, 0, 0)
    cl_action.CommonAddStateCount(oTarget, oLifeCycle, 33510, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })), (lambda *a: 600 + 200 * Func429(*a, **{
'sArg': 'TalentLevel' })))


class CState(cl_state.CState):
    m_SID = 33510
    m_Name = '伤害状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_ALL_NOSELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': (lambda *a: 100 / (1 + Func745(*a, **{
'iType': 2 }) / 10000)) }
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        13: CallBack13 }

