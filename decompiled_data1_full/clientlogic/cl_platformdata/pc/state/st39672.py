# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39672.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39672.pyc
# Source Generated with Decompyle++
# File: st39672.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ARMOR_RADIO_SUB, DEFEND_TREND_ARMOR, OBJ_SELF, SHIELD_RADIO_SUB, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func437, Func597

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'AddMoveSpeed' })), 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 7, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'CalRatio' })),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'AddNum' })) })
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'MoveSpeed', -1, 0, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
        cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)
    if oLifeCycle.m_Owner.GetArgValue('RelieveLimit'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 9, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillMoveSpeed', (lambda *a: max(0, Func404(*a) - Func429(*a, **{
'sArg': 'MoveSpeedMax' }))))
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'SpillMoveSpeed'):
        if not cl_evact.EventCBGetCustomData(oTarget, oEventCB, 'RelieveLimit39672'):
            cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: int(cl_action.CommonGetOwnerAttrBaseValue(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * (100 + Func429(*a, **{
'sArg': 'MoveSpeedMax' })))))
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: (Func437(*a, **{
'sKey': 'SpillMoveSpeed' }) // Func429(*a, **{
'sArg': 'CalRatio' })) * Func429(*a, **{
'sArg': 'AddNum' }) * 100), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillMoveSpeed', (lambda *a: max(0, Func404(*a) - Func429(*a, **{
'sArg': 'MoveSpeedMax' }))))
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'SpillMoveSpeed'):
        if not cl_evact.EventCBGetCustomData(oTarget, oEventCB, 'RelieveLimit39672'):
            cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: int(cl_action.CommonGetOwnerAttrBaseValue(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * (100 + Func429(*a, **{
'sArg': 'MoveSpeedMax' })))))
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: (Func437(*a, **{
'sKey': 'SpillMoveSpeed' }) // Func429(*a, **{
'sArg': 'CalRatio' })) * Func429(*a, **{
'sArg': 'AddNum' }) * 100), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)


def CallBack6(oEventCB, oTarget):
    if oTarget.GetShieldStatus() == 0:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 39673, 300, { }, 0)
        cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')


def CallBack7(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 39673):
        cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillMoveSpeed', (lambda *a: max(0, Func404(*a) - Func429(*a, **{
'sArg': 'MoveSpeedMax' }))))
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'SpillMoveSpeed'):
            if not cl_evact.EventCBGetCustomData(oTarget, oEventCB, 'RelieveLimit39672'):
                cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: int(cl_action.CommonGetOwnerAttrBaseValue(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * (100 + Func429(*a, **{
'sArg': 'MoveSpeedMax' })))))
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: (Func437(*a, **{
'sKey': 'SpillMoveSpeed' }) // Func429(*a, **{
'sArg': 'CalRatio' })) * Func429(*a, **{
'sArg': 'AddNum' }) * 100), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, 0, 0)


def CallBack8(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 39673):
        cl_action.CommonClearForceAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed')
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func597(*a)))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SpillMoveSpeed', (lambda *a: max(0, Func404(*a) - Func429(*a, **{
'sArg': 'MoveSpeedMax' }))))
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'SpillMoveSpeed'):
            if not cl_evact.EventCBGetCustomData(oTarget, oEventCB, 'RelieveLimit39672'):
                cl_action.CommonForceSetAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: int(cl_action.CommonGetOwnerAttrBaseValue(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed') * (100 + Func429(*a, **{
'sArg': 'MoveSpeedMax' })))))
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: (Func437(*a, **{
'sKey': 'SpillMoveSpeed' }) // Func429(*a, **{
'sArg': 'CalRatio' })) * Func429(*a, **{
'sArg': 'AddNum' }) * 100), 0)
        else:
            cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, 0, 0)


def CallBack9(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonListenHPThreshold(oTarget, oEventCB.GetCBLifeCycle(), 0, ARMOR_RADIO_SUB, 6)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 7, 0, 0)
    else:
        cl_action.CommonListenHPThreshold(oTarget, oEventCB.GetCBLifeCycle(), 0, SHIELD_RADIO_SUB, 6)
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 8, 0, 0)


class CState(cl_state.CState):
    m_SID = 39672
    m_Name = '合理移速'
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
        4: CallBack4,
        6: CallBack6,
        7: CallBack7,
        8: CallBack8,
        9: CallBack9 }

