# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33714.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33714.pyc
# Source Generated with Decompyle++
# File: st33714.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func402, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'EnergyCost' }) / 100), None)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 10:
        cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) // 10) * (Func402(*a) + 1) / 100), 0, DAM_USE_HP)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (-cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) // 10) * 10, None)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (Func402(*a) - 1) * Func304(*a, **{
'sAttr': 'HP' }) * 0.05), 0, 0, '')


def CallBack3(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: (Func402(*a) - 1) * Func304(*a, **{
'sAttr': 'HP' }) * 0.05) }, 33714)


class CState(cl_state.CState):
    m_SID = 33714
    m_Name = '#NT#狮子生命之力'
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
        2: CallBack2,
        3: CallBack3 }

