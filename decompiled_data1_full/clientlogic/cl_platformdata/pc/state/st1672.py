# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1672.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1672.pyc
# Source Generated with Decompyle++
# File: st1672.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ArmorMax', -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ShieldMax', -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }))) > 100:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetShieldRatio(oTarget, oEventCB) == 100 or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: max(0, Func304(*a, **{
'sAttr': 'ArmorMax' }) - 100))):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: max(int(Func304(*a, **{
'sAttr': 'HPMax' }) * -2 / 100 + 0), int(Func304(*a, **{
'sAttr': 'HP' }) * -100 / 100 + 1))))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.GetShieldRatio(oTarget, oEventCB) == 100 or cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'Armor' }))) > cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: max(0, Func304(*a, **{
'sAttr': 'ArmorMax' }) - 100))):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 100 / 100 + 0))
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }))) <= 0 and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))) <= 0 and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1672
    m_Name = '#NT#安全气囊（怪物遗物）'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

