# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1800.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1800.pyc
# Source Generated with Decompyle++
# File: st1800.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_SWITCHWEAPON, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func309, Func437, Func517

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTBULLET, -1, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 3, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_SWITCHWEAPON, 3, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: (Func309(*a) / (Func517(*a) * 0.1)) * 100), 'st1800bullets')
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 1800, 'st1800bullets') >= 100:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'st1800bullets' }) / 100))


def CallBack3(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'st1800bullets', 0)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) * 1000, 0, DAM_TYPE_WEAPON, '')


class CState(cl_state.CState):
    m_SID = 1800
    m_Name = '顺水推舟'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
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
        1: CallBack1,
        3: CallBack3,
        5: CallBack5 }

