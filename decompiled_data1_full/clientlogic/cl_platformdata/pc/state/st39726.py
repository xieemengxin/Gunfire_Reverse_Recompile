# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39726.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39726.pyc
# Source Generated with Decompyle++
# File: st39726.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429, Func853

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 1070):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39727, 0, 1, {
            'AdditionDam': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }) + Func853(*a, **{
'iState': 39729 }) * cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 39726, 'ExtraSourceDam', 0, 0)) }, 0, 0, None)
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20030):
        cl_evact.EventCBChangeStateDelayTime(oTarget, oEventCB, 0, (lambda *a: -(Func429(*a, **{
'sArg': 'AbnormalSourceDam' }) + Func853(*a, **{
'iState': 39729 }) * cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 39726, 'ExtraSourceDam', 0, 0))), 1)
    elif cl_evcon.CheckTargetAddState(oTarget, oEventCB, 20031):
        cl_evact.EventCBUpdateSpreadAbnormalDam(oTarget, oEventCB, 0, (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }) + Func853(*a, **{
'iState': 39729 }) * cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 39726, 'ExtraSourceDam', 0, 0)))


def CallBack3(oEventCB, oTarget):
    if cl_condition.CheckSceneFightMonster(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
            1070: 1 }, 1, 1, 0, 1)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 39727, 0, 1, {
            'AdditionDam': (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }) + Func853(*a, **{
'iState': 39729 }) * cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 39726, 'ExtraSourceDam', 0, 0)) }, 0, 0, None)
        cl_evact.EventGetAllMonsterWithStateByTargetScene(oTarget, oEventCB, {
            20030: 1 }, 1, 1, 0, 1)
        cl_evact.EventCBChangeTargetStateDelayTime(oTarget, oEventCB, 20030, 0, (lambda *a: -(Func429(*a, **{
'sArg': 'AbnormalSourceDam' }) + Func853(*a, **{
'iState': 39729 }) * cl_action.CommonGetStateMaxArgsDict(oTarget, oEventCB.GetCBLifeCycle(), 39726, 'ExtraSourceDam', 0, 0))))


class CState(cl_state.CState):
    m_SID = 39726
    m_Name = '#NT#元素专精组件'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

