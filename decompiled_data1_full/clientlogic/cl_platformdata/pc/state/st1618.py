# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1618.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1618.pyc
# Source Generated with Decompyle++
# File: st1618.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MG_SOURCE_KILLMONSTER, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_MONSTER) and cl_evcon.CheckTargetPointBaseMonsters(oTarget, oEventCB, {
        3004: 1,
        3282: 1 }):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 65:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            cl_evact.CommonCBTargetDropReward(oTarget, oEventCB, {
                1001: 1 }, {
                1001: 10000 }, 0, MG_SOURCE_KILLMONSTER, 0, 1)


class CState(cl_state.CState):
    m_SID = 1618
    m_Name = '#NT#幸存者掉落武器计数'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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

