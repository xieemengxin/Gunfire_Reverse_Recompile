# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7145.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7145.pyc
# Source Generated with Decompyle++
# File: st7145.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_HARDNESS, MONSTER_PART_SHIELD, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -6000, 0, '')


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_SHIELD):
        cl_evact.EventCBAddHitPart(oTarget, oEventCB, DAM_TYPE_HARDNESS)


class CState(cl_state.CState):
    m_SID = 7145
    m_Name = '#NT#轮回9喷火怪-躯体减伤被动'
    m_DieRemove = 1
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

