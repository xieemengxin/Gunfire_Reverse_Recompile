# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32945.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32945.pyc
# Source Generated with Decompyle++
# File: st32945.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, oLifeCycle.m_Owner.GetArgValue('StateCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 15)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB) == 0 and cl_evcon.CheckRandom(oTarget, oEventCB, 100, cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle())):
        cl_evact.PassiveExtBulletUse(oTarget, oEventCB, 1)


class CState(cl_state.CState):
    m_SID = 32945
    m_Name = '#NT#后备能源特殊效果'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
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

