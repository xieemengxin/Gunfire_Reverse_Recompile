# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32561.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32561.pyc
# Source Generated with Decompyle++
# File: st32561.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckMonsterType(oTarget, oEventCB):
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1447, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32549, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1448, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32550, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1449, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32551, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1450, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32552, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1451, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32553, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1452, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32554, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1454, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32556, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1453, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32555, 1000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1509, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32613, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1510, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32614, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1540, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32680, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1541, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32681, 6000, { }, None)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1455, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32557, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1456, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32558, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1457, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32559, 6000, { }, None)
        elif cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1458, 0, 0, None, None):
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32560, 6000, { }, None)


class CState(cl_state.CState):
    m_SID = 32561
    m_Name = '#NT#狩猎季节-玩家'
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

