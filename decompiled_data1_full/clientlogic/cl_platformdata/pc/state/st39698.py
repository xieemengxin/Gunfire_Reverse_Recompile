# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39698.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39698.pyc
# Source Generated with Decompyle++
# File: st39698.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func247, Func402, Func404, Func429, Func780

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CommonCheckItemTmpData(oTarget, oLifeCycle, 'Level') == cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func247(*a))):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func780(*a, **{
'sKey': 'Count' })))
    else:
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 15)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    cl_action.StateRefreshStateExtraInfo(oTarget, oLifeCycle, {
        'ExcessiveDam': (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' })) })
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) == 4:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSourceItemTmpData(oTarget, oLifeCycle, 'Level', (lambda *a: Func247(*a)))
    cl_action.CommonSetSourceItemTmpData(oTarget, oLifeCycle, 'Count', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_FIGHT) or cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS) or cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_HALL):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 15)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'DamRatio' }) * Func404(*a) * 100), 0, 0, 1, 1)
    if not cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB):
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -1, 0)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()) == 0 and cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)
        cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 300)


class CState(cl_state.CState):
    m_SID = 39698
    m_Name = '主要技能-魔力激涌'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
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
        1: CallBack1,
        2: CallBack2 }

