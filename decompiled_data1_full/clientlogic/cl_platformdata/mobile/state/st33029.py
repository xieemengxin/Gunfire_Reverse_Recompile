# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33029.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33029.pyc
# Source Generated with Decompyle++
# File: st33029.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func437, Func598, Func664

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Grade' }))) >= 2:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, -1, 1, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 9, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, -1, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, -1, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckReason(oTarget, oEventCB, 'ExchangeRewardChooseTalentGame', None):
        cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ServantEndlessAdd', 1)
        cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)
        cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: 2000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)


def CallBack1(oEventCB, oTarget):
    cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ServantEndlessAdd', 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: 2000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckReason(oTarget, oEventCB, 'ExchangeRewardChooseTalentGame', None):
        cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ServantEndlessAdd', 1)
        cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)
        cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: Func598(*a, **{
'sKey': 'ServantEndlessAdd' }) * 2000 + max(0, int(Func437(*a, **{
'sKey': 'ServantEndlessAddExt' }))) * 2000), 1)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ServantEndlessAdd', 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: Func598(*a, **{
'sKey': 'ServantEndlessAdd' }) * 2000 + max(0, int(Func437(*a, **{
'sKey': 'ServantEndlessAddExt' }))) * 2000), 1)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, (lambda *a: Func664(*a)), 33029, 'ExtAttCount')
    cl_action.CommonAddSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'ServantEndlessAddExt', 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: Func598(*a, **{
'sKey': 'ServantEndlessAdd' }) * 2000 + max(0, int(Func437(*a, **{
'sKey': 'ServantEndlessAddExt' }))) * 2000), 1)


def CallBack8(oEventCB, oTarget):
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: 2000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)


def CallBack9(oEventCB, oTarget):
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', 0, (lambda *a: Func598(*a, **{
'sKey': 'ServantEndlessAdd' }) * 2000 + max(0, int(Func437(*a, **{
'sKey': 'ServantEndlessAddExt' }))) * 2000), 1)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: 4000 * Func598(*a, **{
'sKey': 'ServantEndlessAdd' })), 1)


class CState(cl_state.CState):
    m_SID = 33029
    m_Name = '#NT#御灵师无尽模式机甲成长兼容'
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        8: CallBack8,
        9: CallBack9 }

