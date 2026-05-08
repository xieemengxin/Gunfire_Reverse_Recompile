# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32294.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32294.pyc
# Source Generated with Decompyle++
# File: st32294.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_WEAPON, OBJ_SELF, PF_SUBMSG_COMMON, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1412, 1, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1413, 1, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * (Func402(*a) * 1000 + 1000)), 0, DAM_TYPE_WEAPON, None, 0)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * (Func402(*a) * 1000 + 1000)), 0, DAM_TYPE_PERFORM, None, 0)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1670, 1, 0):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * (Func402(*a) * 1000 + 1000)), 0, DAM_TYPE_PERFORM, None, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32294
    m_Name = '电流虹击'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

