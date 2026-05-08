# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39705.pyc
# Source Generated with Decompyle++
# File: st39705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 218):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PFNODEKILL, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckMainPerform(oTarget, oEventCB, 1) and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7141, 1, 0) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventCBSubTargetCareerPerformColdTime(oTarget, oEventCB, 0, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ReStoreRatio'))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Probability') and cl_evcon.CheckRandom(oTarget, oEventCB, 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Probability')):
            cl_action.CommonAddCareerPfTempUseTimes(oTarget, oEventCB.GetCBLifeCycle(), 1, 1, 1, 1)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Probability') and cl_evcon.CheckRandom(oTarget, oEventCB, 100, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Probability')):
        cl_action.CommonAddCareerPfTempUseTimes(oTarget, oEventCB.GetCBLifeCycle(), 1, 1, 1, 1)


class CState(cl_state.CState):
    m_SID = 39705
    m_Name = '疾风连环'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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
        3: CallBack3 }

