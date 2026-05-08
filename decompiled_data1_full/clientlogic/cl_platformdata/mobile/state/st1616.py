# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1616.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1616.pyc
# Source Generated with Decompyle++
# File: st1616.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func207, Func3, Func364, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTWARCASH, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMSG_PHASESTART, -1, 2)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 2)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: -Func364(*a) // 100), None)
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(-Func364(*a)),
'b': 100 })), 'st1616_WarCash')
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 1616, 'st1616_WarCash') >= 100:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -100, 'st1616_WarCash')
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 100), 0, 0, '')


def CallBack2(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) > 500:
        cl_action.CommonAddWarCash(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -(Func207(*a) - 500)))


class CState(cl_state.CState):
    m_SID = 1616
    m_Name = '挥金如土(灵界狂潮）'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

