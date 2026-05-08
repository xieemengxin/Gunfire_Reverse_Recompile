# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1731.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1731.pyc
# Source Generated with Decompyle++
# File: st1731.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, SKILLCACHE_INT, STATE_ADD_LONGORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_BUILD, WARRIOR_ELITE, WARRIOR_NORBOX, WARRIOR_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1735, 0, 0, None, None) == 0 and cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_INT) and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9016, 1, 0):
        if cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_NORMAL):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1732, 0, 0, { }, 1, None, None)
        elif cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_ELITE) or cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_NORBOX):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1733, 0, 0, { }, 1, None, None)
        elif cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_BOSS):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1734, 0, 0, { }, 1, None, None)
        elif cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_BUILD):
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 1732, 0, 0, { }, 1, None, None)


class CState(cl_state.CState):
    m_SID = 1731
    m_Name = '机瞄步枪13050状态分发'
    m_DieRemove = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
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
        0: CallBack0 }

