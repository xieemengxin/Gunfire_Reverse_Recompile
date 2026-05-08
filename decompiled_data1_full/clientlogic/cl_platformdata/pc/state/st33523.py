# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33523.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33523.pyc
# Source Generated with Decompyle++
# File: st33523.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_THROWPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })) })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })), 0, 1, 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0) == 0:
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })), 0, 1, 0)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func429(*a, **{
'sArg': 'DamAdd' })), 0, '')
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33523
    m_Name = '强力一击'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
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

