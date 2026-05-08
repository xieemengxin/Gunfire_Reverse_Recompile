# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33458.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33458.pyc
# Source Generated with Decompyle++
# File: st33458.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EXECUTETYPE_SUIT_EFFECT, OBJ_ENEMY, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_NORBOX, WARRIOR_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetSideType(oTarget, oEventCB, OBJ_ENEMY):
            if cl_evcon.GetVictimHPRatio(oTarget, oEventCB) < 10:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBTargetDeath(oTarget, oEventCB, EXECUTETYPE_SUIT_EFFECT)
            elif cl_evcon.GetVictimHPRatio(oTarget, oEventCB) < 20 and cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BOSS) == 0 and cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX) == 0:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBTargetDeath(oTarget, oEventCB, EXECUTETYPE_SUIT_EFFECT)
            elif cl_evcon.GetVictimHPRatio(oTarget, oEventCB) < 40 and cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORMAL) and cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORBOX) == 0:
                cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
                cl_evact.EventCBTargetDeath(oTarget, oEventCB, EXECUTETYPE_SUIT_EFFECT)


class CState(cl_state.CState):
    m_SID = 33458
    m_Name = '高阶审判'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
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

