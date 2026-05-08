# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33917.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33917.pyc
# Source Generated with Decompyle++
# File: st33917.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREVERTIGO, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 1070)
    cl_action.CommonRemoveState(oTarget, oLifeCycle, 20039)
    cl_action.CommonAddLogicKey(oTarget, oLifeCycle, FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.CommonMonsterSwitch(oTarget, oLifeCycle, 23411, {
        4163: 1,
        4166: 1,
        4307: 1 }, 'MonsterNear.BoxNearRunNewS6', { })
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33917
    m_Name = '#NT#咯尔刻之力变猪状态'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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

