# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32113.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32113.pyc
# Source Generated with Decompyle++
# File: st32113.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func402, Func512

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) == 0:
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st32113', None) >= 1 or cl_evcon.StateCBCheckHasSelf(oTarget, oEventCB):
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st32113', 1, None)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func402(*a) * 10000 + 20000), 0, DAM_TYPE_WEAPON, '')
            if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 10, None, None, None, None)
                cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            else:
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 10, None, None, None, None)
                cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventTargetSputterDamage(oTarget, oEventCB, (lambda *a: Func402(*a) * 25 + 25), 1, None, None, None, None, None, None, None, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventTargetSputterDamage(oTarget, oEventCB, (lambda *a: (Func402(*a) * 25 + 25) * Func512(*a, **{
'sAttr': 'CrazyEff' }) / 10000), 1, None, None, None, None, None, None, None, None)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) == 0:
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st32113', None) >= 1 or cl_evcon.StateCBCheckHasSelf(oTarget, oEventCB):
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st32113', 1, None)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func402(*a) * 10000 + 20000), 0, DAM_TYPE_WEAPON, '')
            if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 10, None, None, None, None)
                cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            else:
                cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
                cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 15, WARRIOR_MONSTER, 1, 1, 10, None, None, None, None)
                cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32113
    m_Name = '聚光神剑'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

