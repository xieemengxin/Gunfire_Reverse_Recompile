# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33677.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33677.pyc
# Source Generated with Decompyle++
# File: st33677.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, OBJ_SELF, PF_TYPE_CONSHOOT, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, 30)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'ST33677', 1, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST33677', 1):
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK_END, -1, 3, 0, 0)
        if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, 0):
            cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 30)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 30)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33677
    m_Name = '快速换弹'
    m_IsShow = 1
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

