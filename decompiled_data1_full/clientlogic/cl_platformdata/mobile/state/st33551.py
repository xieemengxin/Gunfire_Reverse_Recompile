# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33551.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33551.pyc
# Source Generated with Decompyle++
# File: st33551.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func437, Func748

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBGetTargetByEventMonster(oTarget, oEventCB)
    if cl_evcon.EventCBCheckIsMonsterGroup(oTarget, oEventCB, {
        39211: 1 }):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33551ID', cl_evact.EventGetTargeID(oTarget, oEventCB))
        cl_evact.EventCBListenTargetMsgCallBack(oTarget, oEventCB, cl_msgcenter.MSG_WAR_REMOVEOBJ, -1, 5, 0)
        cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
            33510: 1 }, 1, 1, 1, 0)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33551Add', 0)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33551Add') and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func748(*a))):
            cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': '33551ID' })))
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33510, (lambda *a: Func748(*a)), 1, {
                'StateCount': (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })),
                'AbnormalSourceDam': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' })),
                'Att': (lambda *a: Func429(*a, **{
'sArg': 'Att' })),
                'TalentLevel': (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBCheckIsMonsterGroup(oTarget, oEventCB, {
        39211: 1 }) and cl_evcon.CheckTargetHasStateByAttacker(oTarget, oEventCB, 33510, (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }))):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33551Add', 1)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
        33510: 1 }, 1, 1, 1, 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33551Add', 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33551Add') and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func748(*a))):
        cl_evact.EventCBSetTargetByID(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': '33551ID' })))
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33510, (lambda *a: Func748(*a)), 1, {
            'StateCount': (lambda *a: Func429(*a, **{
'sArg': 'StateCount' })),
            'AbnormalSourceDam': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' })),
            'Att': (lambda *a: Func429(*a, **{
'sArg': 'Att' })),
            'TalentLevel': (lambda *a: Func429(*a, **{
'sArg': 'TalentLevel' })) }, 2, 0, 0)


class CState(cl_state.CState):
    m_SID = 33551
    m_Name = '虬蛇画地为牢效果管理'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        5: CallBack5 }

