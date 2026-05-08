# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1665.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1665.pyc
# Source Generated with Decompyle++
# File: st1665.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func302, Func304, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, 25750)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Shield' }))) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) < cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }))) or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func404(*a) * 1 + 0)) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ShieldMax' }) * 30 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, -1, None)
        cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ArmorMax' }) * 30 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_ARMOR, 0, -1, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1717, 100, { }, None)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 1, 0)


class CState(cl_state.CState):
    m_SID = 1665
    m_Name = '#NT#幽魂皮肤（怪物遗物）'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 600,
        'firsttime': 100,
        'cnt': 3 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

