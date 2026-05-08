# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33528.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33528.pyc
# Source Generated with Decompyle++
# File: st33528.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func437, Func517

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'CntMax', (lambda *a: Func517(*a)))


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4508):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func208(*a)), None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CntMax'):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func437(*a, **{
'sKey': 'CntMax' })), None)
            cl_action.CommonSendStateCountChangeMessage(oTarget, oEventCB.GetCBLifeCycle())


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckCostBulletType(oTarget, oEventCB, 4508):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func215(*a)), None)
        if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'CntMax'):
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func437(*a, **{
'sKey': 'CntMax' })), None)
            cl_action.CommonSendStateCountChangeMessage(oTarget, oEventCB.GetCBLifeCycle())


class CState(cl_state.CState):
    m_SID = 33528
    m_Name = '#NT#消耗弹夹条件'
    m_IsShow = 1
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
        1: CallBack1,
        2: CallBack2 }

