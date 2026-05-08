# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39677.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39677.pyc
# Source Generated with Decompyle++
# File: st39677.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_HIDE, OBJECT_SERVANT, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 3)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeServantAttr(oTarget, oLifeCycle, 'AttSpeed', (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'PerAttSpeedMul' })), 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func404(*a) * Func429(*a, **{
'sArg': 'PerAttSpeedMul' }) / 100) })
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('MaxCount'):
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'CanReduceCD', 1)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, 7141, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'AttRangeMul' })), OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, 7142, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'AttRangeMul' })), OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, 7143, 'Radius', 0, (lambda *a: Func429(*a, **{
'sArg': 'AttRangeMul' })), OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, 7148, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'AttRangeMul' })), OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, 7150, 'AttDistance', 0, (lambda *a: Func429(*a, **{
'sArg': 'AttRangeMul' })), OBJECT_SERVANT, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7142: 1,
        7141: 1,
        7143: 1 }, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, 'HadHit') == 0:
        cl_evact.EventCBSetSkillCustomInfo(oTarget, oEventCB, 'HadHit', 1)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanReduceCD'):
            cl_evact.EventGetTargetByServant(oTarget, oEventCB)
            cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 7148, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReduceCD'), 0)
            cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 7150, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReduceCD'), 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'CanReduceCD', 0)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7141, 'AttDistance', 0, 0, OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7142, 'AttDistance', 0, 0, OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7143, 'Radius', 0, 0, OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7148, 'AttDistance', 0, 0, OBJECT_SERVANT, None)
        cl_action.CommonChangePerformAttrFromOwn(oTarget, oEventCB.GetCBLifeCycle(), 7150, 'Radius', 0, 0, OBJECT_SERVANT, None)


class CState(cl_state.CState):
    m_SID = 39677
    m_Name = '#NT#铁翼升级战斗'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

