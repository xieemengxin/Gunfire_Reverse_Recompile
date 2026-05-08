# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33664.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33664.pyc
# Source Generated with Decompyle++
# File: st33664.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437, Func651, Func752

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    if oLifeCycle.m_Owner.GetArgValue('IsLuckyHit') == 1:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: max(0, (Func752(*a, **{
'iWandSID': 1018,
'iDefault': 0 }) // 20) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StatusEffect'))))
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 100), 0, DAM_TYPE_WEAPON, '')


def CallBack1(oEventCB, oTarget):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('IsLuckyHit') == 1 and cl_condition.CommonGetSourceWandCount(oTarget, oEventCB.GetCBLifeCycle()) >= 300:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 100)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ChangeDesc') == 0:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ChangeDesc', 1)
            cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'SrcLV': (lambda *a: Func437(*a, **{
'sKey': 'ChangeDesc' })) })


def CallBack3(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'StateSID' }))) == 33584 and cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ChangeDesc'):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ChangeDesc', 0)
        cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': (lambda *a: Func437(*a, **{
'sKey': 'ChangeDesc' })) })


class CState(cl_state.CState):
    m_SID = 33664
    m_Name = '令牌专属词条'
    m_IsShow = 1
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

