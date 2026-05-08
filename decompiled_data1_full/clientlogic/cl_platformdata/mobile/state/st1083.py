# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1083.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1083.pyc
# Source Generated with Decompyle++
# File: st1083.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MAIN_DEBUFF, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF, 2, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'DebuffProb', 0, (lambda *a: Func404(*a) * 5000 + 0))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st1083', 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 1083
    m_Name = '铭刻'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        1: CallBack1,
        2: CallBack2 }

