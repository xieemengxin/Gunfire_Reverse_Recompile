# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1080.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1080.pyc
# Source Generated with Decompyle++
# File: st1080.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, PF_SUBMSG_FILLBULLET, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func409

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Att', 0, (lambda *a: Func404(*a) * 1000 + 0))
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oLifeCycle, 4908):
        cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Stability', (lambda *a: Func404(*a) * 5 + 0), 0)
        cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'LuckyHit', (lambda *a: Func404(*a) * 1 + 0), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        if cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 4907):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func404(*a) * 0.5 + 0))
        elif cl_evcon.CheckWeaponHasInscription(oTarget, oEventCB, 4959):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func409(*a) + 0))
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1080
    m_Name = '炎魔传说'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 99
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

