# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33492.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33492.pyc
# Source Generated with Decompyle++
# File: st33492.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_BUYGOODS, LEVEL_TYPE_HIDE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, SUIT_HANDLE_COINBANK
from cl_newformula import Func247, Func727

def StateActAction(oTarget, oLifeCycle):
    if not cl_action.CommonGetSeasonSuitArg(oTarget, oLifeCycle, 15191, '33492First', 1):
        cl_action.CommonSetSeasonSuitArg(oTarget, oLifeCycle, 15191, '33492First', 1, 1)
        cl_action.CommonSetSeasonSuitArg(oTarget, oLifeCycle, 15191, '33492Count', 500, 1)
    cl_action.CommonSendSuitHandleInfo(oTarget, oLifeCycle, SUIT_HANDLE_COINBANK, {
        1: (lambda *a: Func727(*a, **{
'iSuit': 15191,
'sKey': '33492Count' })) }, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 3)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLOGIN, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Count', 1) < 999999:
        cl_action.CommonChangeSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Count', 5, 1)
        if cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Count', 1) > 999999:
            cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Count', 999999, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_COINBANK, {
            1: (lambda *a: Func727(*a, **{
'iSuit': 15191,
'sKey': '33492Count' })) }, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func247(*a))) != cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Level', 1):
        cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15191, '33492Level', (lambda *a: Func247(*a)), 1)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Show', 1)
        cl_evact.EventCBAddCash(oTarget, oEventCB, (lambda *a: Func727(*a, **{
'iSuit': 15191,
'sKey': '33492Count' })), 0, JUMPFIGURE_BUYGOODS, 0, 1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'Show'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Show', 0)
        cl_evact.EventCBSendNotify(oTarget, oEventCB, 1, 9680, {
            '$cash': (lambda *a: Func727(*a, **{
'iSuit': 15191,
'sKey': '33492Count' })) })


def CallBack4(oEventCB, oTarget):
    cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_COINBANK, {
        1: (lambda *a: Func727(*a, **{
'iSuit': 15191,
'sKey': '33492Count' })) }, None)


class CState(cl_state.CState):
    m_SID = 33492
    m_Name = '铜币银行'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

