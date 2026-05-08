# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33509.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33509.pyc
# Source Generated with Decompyle++
# File: st33509.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, SUIT_HANDLE_EACHGETWHAT
from cl_newformula import Func332, Func404, Func727

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33509, (lambda *a: Func332(*a)), None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, SUIT_HANDLE_EACHGETWHAT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 9, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLOGIN, -1, 13, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 13, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBGetSeasonSuitOptData(oTarget, oEventCB, 0) == 1:
        cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1, 1)
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 1 }, 33509)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 1)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * 1500), 0, 0, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 1,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
    elif cl_evcon.EventCBGetSeasonSuitOptData(oTarget, oEventCB, 0) == 2:
        cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 2, 1)
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 2 }, 33509)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, 0, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func404(*a) * 1500), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func404(*a) * 1500), 0)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 2,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
    elif cl_evcon.EventCBGetSeasonSuitOptData(oTarget, oEventCB, 0) == 3:
        cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 3, 1)
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 3 }, 33509)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), 0, 0, 0, 1)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func404(*a) * 500), 0, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 3,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)


def CallBack9(oEventCB, oTarget):
    cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33509, (lambda *a: Func332(*a)), None)
    if cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 1:
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * 1500), 0, 0, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 1,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
    elif cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 2:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func404(*a) * 1500), 0)
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func404(*a) * 1500), 0)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 2,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
    elif cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 3:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func404(*a) * 500), 0, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 3,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)


def CallBack13(oEventCB, oTarget):
    if cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1):
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': (lambda *a: Func727(*a, **{
'iSuit': 15213,
'sKey': 'ST33509' })) }, 33509)
        if cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 1:
            cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * 1500), 0, 0, 1)
            cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
                'Select': 1,
                'Dam': (lambda *a: Func404(*a) * 15),
                'Shield': (lambda *a: Func404(*a) * 15),
                'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
        elif cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 2:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func404(*a) * 1500), 0)
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func404(*a) * 1500), 0)
            cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
                'Select': 2,
                'Dam': (lambda *a: Func404(*a) * 15),
                'Shield': (lambda *a: Func404(*a) * 15),
                'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
        elif cl_action.CommonGetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1) == 3:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func404(*a) * 500), 0, 1)
            cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
                'Select': 3,
                'Dam': (lambda *a: Func404(*a) * 15),
                'Shield': (lambda *a: Func404(*a) * 15),
                'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)
    else:
        cl_action.CommonSetSeasonSuitArg(oTarget, oEventCB.GetCBLifeCycle(), 15213, 'ST33509', 1, 1)
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'SrcLV': 1 }, 33509)
        cl_action.CommonChangeBaseDamRatio(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func404(*a) * 1500), 0, 0, 1)
        cl_action.CommonSendSuitHandleInfo(oTarget, oEventCB.GetCBLifeCycle(), SUIT_HANDLE_EACHGETWHAT, {
            'Select': 1,
            'Dam': (lambda *a: Func404(*a) * 15),
            'Shield': (lambda *a: Func404(*a) * 15),
            'MoveSpeed': (lambda *a: Func404(*a) * 5) }, None)


class CState(cl_state.CState):
    m_SID = 33509
    m_Name = '各得其宜'
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
        9: CallBack9,
        13: CallBack13 }

