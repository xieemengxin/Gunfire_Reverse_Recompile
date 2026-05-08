# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1785.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1785.pyc
# Source Generated with Decompyle++
# File: st1785.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1818, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1819, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1820, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, None)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1818, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1819, 0)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 1820, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 1:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 2:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, -2500, 0, 0, '')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 3:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 10000, 0, 0, '')


def CallBack4(oEventCB, oTarget):
    if not cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 1:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, -2000, 0, 0, '')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 2:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 4000, 0, 0, '')
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 3:
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 8000, 0, 0, '')


def CallBack8(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 1:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1818, 0, { }, 0)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 2:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1819, 0, { }, 0)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 3:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1820, 0, { }, 0)


class CState(cl_state.CState):
    m_SID = 1785
    m_Name = '#NT#枪火共生'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        4: CallBack4,
        8: CallBack8 }

