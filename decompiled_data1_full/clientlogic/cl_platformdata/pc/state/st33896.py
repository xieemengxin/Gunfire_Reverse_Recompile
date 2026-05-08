# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33896.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33896.pyc
# Source Generated with Decompyle++
# File: st33896.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_TYPE_THROW, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func604

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckHero(oTarget, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 1, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= oLifeCycle.m_Owner.GetArgValue('AttackTimes'):
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'MulReply', (lambda *a: Func404(*a) // Func429(*a, **{
'sArg': 'AttackTimes' })))
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func404(*a) % Func429(*a, **{
'sArg': 'AttackTimes' })))
        cl_action.CommonAddBagBullet(oTarget, oLifeCycle, 4508, (lambda *a: Func429(*a, **{
'sArg': 'ReplyTimes' }) * Func429(*a, **{
'sArg': 'MulReply' })), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0) and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8004, 1, 0) == 0:
        cl_evact.EventCBRecordHitTarget(oTarget, oEventCB, 1)
        cl_evact.EventCBSetTargetBySkillHit(oTarget, oEventCB, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBGetMsgInfo(oTarget, oEventCB, 'GardenThrowHit'):
        cl_evact.EventCBRecordHitTarget(oTarget, oEventCB, 1)
        cl_evact.EventCBSetTargetBySkillHit(oTarget, oEventCB, 1)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.EventCBGetVictimHitNumberInCollect(oTarget, oEventCB, 1) == 1:
        if cl_evcon.EventCBGetSkillCustomInfo(oTarget, oEventCB, 'dice51366'):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func604(*a, **{
'sKey': 'dice51366' })), 0)
        else:
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


class CState(cl_state.CState):
    m_SID = 33896
    m_Name = '#NT#S7-灵力回复'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
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
        1: CallBack1,
        3: CallBack3 }

