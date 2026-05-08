# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1133.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1133.pyc
# Source Generated with Decompyle++
# File: st1133.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 3:
        cl_action.StateAddState(oTarget, oLifeCycle, 1780, 0, {
            'LuckyHit': 2 }, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', 1)
    else:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'CollectHitTarget', None) and cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1133
    m_Name = '#NT#铭刻4843连续爆头'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 99999
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
        1: CallBack1 }

