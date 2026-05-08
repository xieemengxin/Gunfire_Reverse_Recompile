# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32374.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32374.pyc
# Source Generated with Decompyle++
# File: st32374.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, VIRTUAL_ITEM_RELIC
from cl_newformula import Func404, Func429, Func598, Func707

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BUYGOODS, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'Damage' })), 0, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckGoodsIsPointItem(oTarget, oEventCB, VIRTUAL_ITEM_RELIC, 0):
        cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'PF5879', 1)
        cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 32374, (lambda *a: Func598(*a, **{
'sKey': 'PF5879' }) * Func707(*a)), None)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 32374, (lambda *a: Func598(*a, **{
'sKey': 'PF5879' }) * Func707(*a)), None)


class CState(cl_state.CState):
    m_SID = 32374
    m_Name = '应有尽有'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

