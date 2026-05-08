# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1150.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1150.pyc
# Source Generated with Decompyle++
# File: st1150.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from math import ceil
from cl_newformula import Func208, Func214, Func404, Func409

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 1, 0, 0)
    if cl_condition.CheckSourceWeaponClassifyTag(oTarget, oLifeCycle, 12):
        cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CheckSourceWeaponClassifyTag(oTarget, oLifeCycle, 12) == 0:
        cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'LuckyHit', (lambda *a: min(100, int(Func404(*a) * 10 / ceil(Func409(*a) * 10 / 100)))), 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a)), None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckBulletChange(oTarget, oEventCB, 11040, 1):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func214(*a)), None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func409(*a))) > 0:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: min(100, int(Func404(*a) * 10 / ceil(Func409(*a) * 10 / 100)))))


class CState(cl_state.CState):
    m_SID = 1150
    m_Name = '#NT#铭刻4858计数加幸运一击'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        2: CallBack2 }

