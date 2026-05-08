# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32622.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32622.pyc
# Source Generated with Decompyle++
# File: st32622.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, COST_BAGBULLET_WEAPON, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CAREERPF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func208, Func215, Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 6, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 32622, 1, 'st32622_lasthit')


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER) and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 25 * Func331(*a, **{
'sid': 5420 })))
        if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None):
            if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5420) >= 3:
                cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32728, 200, { }, None)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
            else:
                cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32728, 300, { }, None)
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        elif cl_evcon.CheckStateStatistics(oTarget, oEventCB, 32622, 'st32622_lasthit') == 1:
            cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: 25 * Func331(*a, **{
'sid': 5420 })))
            if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, None):
                if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5420) >= 3:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32728, 200, { }, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)
                else:
                    cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32728, 300, { }, None)
                    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack5(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func208(*a)), None)


def CallBack6(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func215(*a)), None)


class CState(cl_state.CState):
    m_SID = 32622
    m_Name = '斗转星移'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 1
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 0
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        5: CallBack5,
        6: CallBack6 }

