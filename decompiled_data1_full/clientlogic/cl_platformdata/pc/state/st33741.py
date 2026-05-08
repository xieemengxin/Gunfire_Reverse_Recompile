# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33741.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33741.pyc
# Source Generated with Decompyle++
# File: st33741.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func812, Func813

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, -1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.EventCBCheckAffectedByLion(oTarget, oEventCB, 0, 1, 1):
        cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33741, 'EnhanceLockState', (lambda *a: (Func812(*a, **{
'iState': 8156 }) + Func813(*a, **{
'sid': 8156,
'sAttr': 'LockStateKeepTime' })) // 100))
        cl_evact.EventCBSetStateArgVal(oTarget, oEventCB, 33741, 'LockState', (lambda *a: Func812(*a, **{
'iState': 8155 }) // 100))
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: max(int(Func429(*a, **{
'sArg': 'EnhanceLockState' })), int(Func429(*a, **{
'sArg': 'LockState' })))))
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'BaseLuckyHit' }) + Func404(*a) * Func429(*a, **{
'sArg': 'ExtraLuckyHit' })))


class CState(cl_state.CState):
    m_SID = 33741
    m_Name = '#NT#狮子W1'
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
        0: CallBack0 }

