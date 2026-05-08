# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33247.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33247.pyc
# Source Generated with Decompyle++
# File: st33247.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, OBJ_ATTACK, OBJ_SELF, PF_TYPE_CAREERPF, PF_TYPE_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CAREERPF, 0) or cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 3000, 0, DAM_TYPE_PERFORM, '')


class CState(cl_state.CState):
    m_SID = 33247
    m_Name = '#NT#法杖专属铭刻1技能伤害加成'
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

