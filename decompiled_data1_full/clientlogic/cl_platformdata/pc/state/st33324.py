# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33324.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33324.pyc
# Source Generated with Decompyle++
# File: st33324.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_HOLD, OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func434

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33324, cl_action.CommonGetWeaponPerformArgs(oTarget, oLifeCycle, 5306, 'JQCount'), None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, MAIN_HOLD, 5, 0, 0)
    cl_action.StateAddState(oTarget, oLifeCycle, 33386, 0, { }, cl_action.CommonGetWeaponPerformArgs(oTarget, oLifeCycle, 5306, 'PFAttCnt'))


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle):
        cl_action.StateSwitchAttPerform(oTarget, oLifeCycle, 1)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oTarget, oLifeCycle, 5306, 'JQCount', cl_action.StateGetSelfCount(oTarget, oLifeCycle))
    cl_action.CommonSetWeaponPerformArgs(oTarget, oLifeCycle, 5306, 'PFAttCnt', (lambda *a: Func434(*a, **{
'sid': 33386 })))


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1310: 1 }, 0, 0):
        if not cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33386, 1, 0)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB):
        if not cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oEventCB.GetCBLifeCycle()):
            cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33386, 1, 0)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9704, 0, 0):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    elif cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9705, 0, 0):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33386, 0, None)
        cl_action.StateResetAttPerform(oTarget, oEventCB.GetCBLifeCycle())


def CallBack5(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33324
    m_Name = '#NT#聚能法杖层数'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        5: CallBack5 }

