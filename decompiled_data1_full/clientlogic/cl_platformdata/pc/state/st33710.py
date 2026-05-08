# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33710.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33710.pyc
# Source Generated with Decompyle++
# File: st33710.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, OBJ_VICTIM, SKILL7168, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'NotToEvole', 1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'AttSpeed', oLifeCycle.m_Owner.GetArgValue('AttSpeed'), 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HitRange', 0, 99, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, SKILL7168, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AttCnt'):
        cl_action.CommonSelfDie(oTarget, oEventCB.GetCBLifeCycle())


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7168: 1,
        7169: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddTargetParasiticState(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AttParasiticCnt') + oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraAttParasiticCnt'))


class CState(cl_state.CState):
    m_SID = 33710
    m_Name = '#NT#园丁Q灵佑植物加成状态'
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

