# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32850.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32850.pyc
# Source Generated with Decompyle++
# File: st32850.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction32850 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, TYPE_RELIFE_RESCUE
from cl_newformula import Func304, Func360

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'CanExplosion', 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'CanExplosion', 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckRelifeType(oTarget, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
    if not cl_evcon.EventCBCheckTargetRealDead(oTarget, oEventCB):
        cl_action.CommonUsePerform(oTarget, oEventCB.GetCBLifeCycle(), 7152, { })


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        7153: 1,
        7154: 1 }, 0, 0):
        cl_evact.NextFrameTriggerGroup(oTarget, oEventCB, 4, None)
        cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
        if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
            7153: 1 }, 0, 0):
            cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 1321, (lambda *a: Func360(*a, **{
'sid': 1321,
'sAttr': 'ColdTime' })), 0)
        else:
            cl_evact.EventCBSubTargetPerformColdTime(oTarget, oEventCB, 1322, (lambda *a: Func360(*a, **{
'sid': 1322,
'sAttr': 'ColdTime' })), 0)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' })), 32850, 'HpBeforeDie')
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), { })


class CState(cl_state.CState):
    m_SID = 32850
    m_Name = '#NT#御灵师仆从自爆'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        4: CallBack4 }

