# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1248.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1248.pyc
# Source Generated with Decompyle++
# File: st1248.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, -1, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, None):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st1248', 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1248', None) == 0:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'DebuffProb', 0, (lambda *a: Func404(*a) * 2000 + 20000))


class CState(cl_state.CState):
    m_SID = 1248
    m_Name = '#NT#每日挑战4404元素异常'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

