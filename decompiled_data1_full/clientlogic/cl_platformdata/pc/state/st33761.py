# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33761.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33761.pyc
# Source Generated with Decompyle++
# File: st33761.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', -3000, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1331, 1, 0):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MoveSpeed', 0, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1331, 1, 0):
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST33761', 0):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20000, 0, '')
        elif oTarget.Energy() >= 3000:
            cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), -3000, 0)
            cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'ST33761', 1, 0)
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 20000, 0, '')


class CState(cl_state.CState):
    m_SID = 33761
    m_Name = '#NT#狮子蓄力远程状态'
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
        0: CallBack0,
        1: CallBack1 }

