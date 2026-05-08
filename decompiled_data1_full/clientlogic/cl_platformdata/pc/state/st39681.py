# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39681.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39681.pyc
# Source Generated with Decompyle++
# File: st39681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_SERVANT, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func589, Func634

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackFromOwnByAttr(oTarget, oLifeCycle, 'HPMax', 1, OBJECT_SERVANT)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ExtraHPMax', (lambda *a: Func589(*a) * Func429(*a, **{
'sArg': 'HPAddPerHPMax' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func429(*a, **{
'sArg': 'ExtraHPMax' })), 1)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }) // Func429(*a, **{
'sArg': 'EnhancePerHP' })))
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DamMul', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'PerDamMul' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), 0, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7144, 'Att', 0, (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'Att', 0, (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), OBJECT_SERVANT, 1)
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'OtherMul', (lambda *a: min(Func404(*a) * Func429(*a, **{
'sArg': 'PerOtherMul' }), Func429(*a, **{
'sArg': 'MaxOtherMul' }))))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamMul' }) // 100),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' }) // 100) })
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, (lambda *a: 100 + (Func634(*a, **{
'sAttr': 'HPMax' }) // Func429(*a, **{
'sArg': 'AddSaclePerHP' })) * Func429(*a, **{
'sArg': 'PerScaleAdd' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), 0, 0)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), 0, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7141, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7142, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7143, 'Radius', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7148, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7150, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)


def CallBack2(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'ExtraHPMax', (lambda *a: Func589(*a) * Func429(*a, **{
'sArg': 'HPAddPerHPMax' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func429(*a, **{
'sArg': 'ExtraHPMax' })), 1)
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }) // Func429(*a, **{
'sArg': 'EnhancePerHP' })))
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'DamMul', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'PerDamMul' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Att', (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), 0, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7144, 'Att', 0, (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7151, 'Att', 0, (lambda *a: Func429(*a, **{
'sArg': 'DamMul' })), OBJECT_SERVANT, 1)
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'OtherMul', (lambda *a: min(Func404(*a) * Func429(*a, **{
'sArg': 'PerOtherMul' }), Func429(*a, **{
'sArg': 'MaxOtherMul' }))))
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamMul' }) // 100),
        'cdrate': (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' }) // 100) })
    cl_evact.EventGetTargetByServant(oTarget, oEventCB)
    cl_evact.EventCBChangeTargetModel(oTarget, oEventCB, (lambda *a: 100 + (Func634(*a, **{
'sAttr': 'HPMax' }) // Func429(*a, **{
'sArg': 'AddSaclePerHP' })) * Func429(*a, **{
'sArg': 'PerScaleAdd' })))
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), 0, 0)
    cl_action.CommonChangeServantAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), 0, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7141, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7142, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7143, 'Radius', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 0)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7148, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)
    cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7150, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'OtherMul' })), OBJECT_SERVANT, 1)


class CState(cl_state.CState):
    m_SID = 39681
    m_Name = '战斗核心'
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
        2: CallBack2 }

