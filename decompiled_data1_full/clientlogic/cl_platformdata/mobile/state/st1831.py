# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1831.pyc
# Source Generated with Decompyle++
# File: st1831.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0)
    cl_action.CommonListenServantMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 3:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st1831', 1, None)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st1831', 1)
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 2, 0, 0)
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st1831', 0)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1719, 1, 0) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'st1831' }))):
        cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st1831', 1, None)
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DP, -1)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 7153, 1, 0):
        if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1831', None):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 30000, 0, 0, '')
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBUsePerform(oTarget, oEventCB, 1719, 0, { })


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1719, 1, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st1831', None):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 30000, 0, 0, '')


class CState(cl_state.CState):
    m_SID = 1831
    m_Name = '战斗核心'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 4
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
        2: CallBack2,
        3: CallBack3,
        5: CallBack5 }

