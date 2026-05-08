# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32704.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32704.pyc
# Source Generated with Decompyle++
# File: st32704.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0)
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeHP(oTarget, oEventCB, 100)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -10000, 0)


class CState(statedata.CStateData):
    m_SID = 32704
    m_Name = '#NT#处决大师E6维持'
    m_IsShow = 1
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
        1: CallBack1 }

