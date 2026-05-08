# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33432.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33432.pyc
# Source Generated with Decompyle++
# File: st33432.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DEFEND_TREND_SHIELD, NWARRIOR_DROP_RELIC, OBJ_ATTACK, OBJ_SELF, PF_TYPE_SUITACTIVE, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437, Func718, Func719

def StateActAction(oTarget, oLifeCycle):
    if not cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func719(*a)))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGEBLANKRELICNUM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSUITPERFORM, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 4, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', 0, (lambda *a: 300 * Func404(*a)), 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33432, (lambda *a: -min(6000, int(150 * Func404(*a)))), 'SubCD')
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', (lambda *a: Func437(*a, **{
'sKey': 'SubCD' })), 0, None)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1310, 'ColdTime', (lambda *a: Func437(*a, **{
'sKey': 'SubCD' })), 0)
    cl_action.CommonChangeTargetTypePerformAttr(oTarget, oLifeCycle, PF_TYPE_SUITACTIVE, 'ColdTime', (lambda *a: Func437(*a, **{
'sKey': 'SubCD' })), 0)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: 300 * Func404(*a)), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: 300 * Func404(*a)), 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func718(*a)), None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 1500 * cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    cl_action.CommonChangeCareerPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ColdTime', (lambda *a: Func437(*a, **{
'sKey': 'SubCD' })), 0, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBSetEventPerformAttr(oTarget, oEventCB, 'ColdTime', (lambda *a: Func437(*a, **{
'sKey': 'SubCD' })), 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckEventRecycleDropType(oTarget, oEventCB, NWARRIOR_DROP_RELIC):
        cl_action.CommonAddBlankRelic(oTarget, oEventCB.GetCBLifeCycle(), 1)


class CState(cl_state.CState):
    m_SID = 33432
    m_Name = '无为自化'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

