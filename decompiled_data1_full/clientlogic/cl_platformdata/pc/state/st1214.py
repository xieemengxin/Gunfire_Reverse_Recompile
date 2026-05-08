# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1214.pyc
# Source Generated with Decompyle++
# File: st1214.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    if cl_condition.CheckSourceWeaponClassifyTag(oTarget, oLifeCycle, 12):
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 3, 0, 0)
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 4, 0, 0)
    else:
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if not cl_condition.CheckSourceWeaponClassifyTag(oTarget, oLifeCycle, 12):
        cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'CrazyEff', (lambda *a: Func404(*a) * 2000), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1214', None) == 0 and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB) and cl_evcon.CheckHitWeakness(oTarget, oEventCB, None):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st1214', 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeDamCrazyEff(oTarget, oEventCB, (lambda *a: 2000 * Func404(*a)), 0)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'st1214', 1, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1214', None) == 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    else:
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'st1214', 0, 0)


class CState(cl_state.CState):
    m_SID = 1214
    m_Name = '#NT#铭刻4888'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
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
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

