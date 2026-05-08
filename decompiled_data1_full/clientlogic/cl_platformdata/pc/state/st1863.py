# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1863.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1863.pyc
# Source Generated with Decompyle++
# File: st1863.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckStatistics(oTarget, oLifeCycle, 'TimeCount') > 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetWeaponPerformArgs(oTarget, oLifeCycle, 9093, 'Limit', 5)


def CallBack0(oEventCB, oTarget):
    if (cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9017, 0, 0) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12028, 0, 0)) and cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'AttCount')
        if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'AttCount') >= 10:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AttCount', 0)
            cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TimeCount', 4)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'TimeCount')


def CallBack3(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonSetWeaponPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 9093, 'Limit', (lambda *a: 5 - Func404(*a)))


class CState(cl_state.CState):
    m_SID = 1863
    m_Name = '#NT#追踪步枪铭刻2'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

