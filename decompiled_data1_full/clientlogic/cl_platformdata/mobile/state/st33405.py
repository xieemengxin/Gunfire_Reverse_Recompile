# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33405.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33405.pyc
# Source Generated with Decompyle++
# File: st33405.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ALL, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromWeaponPFBulletPerform(oTarget, oEventCB):
        if cl_evcon.CheckTargetIsSummon(oTarget, oEventCB) == 0 or cl_evcon.CheckTargetPointBaseSummon(oTarget, oEventCB, 1083):
            if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
                cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 3, None)
            else:
                cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


class CState(cl_state.CState):
    m_SID = 33405
    m_Name = '域外神匠(天降大任统计)'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_ALL
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
        0: CallBack0 }

