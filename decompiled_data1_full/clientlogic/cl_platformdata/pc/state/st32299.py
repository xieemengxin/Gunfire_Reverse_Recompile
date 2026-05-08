# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32299.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32299.pyc
# Source Generated with Decompyle++
# File: st32299.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_SNIPER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckWeaponType(oTarget, oEventCB, EQUIP_SNIPER):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 32300, 0, 1, None, None):
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32300, 1, 1, None, None)
        else:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32300, 0, 0, { }, 1, None, None)


class CState(cl_state.CState):
    m_SID = 32299
    m_Name = '#NT#虹积骨销2'
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
        0: CallBack0 }

