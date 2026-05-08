# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32504.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32504.pyc
# Source Generated with Decompyle++
# File: st32504.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func3, Func404, Func428

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 6, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, (lambda *a: (Func208(*a) + Func404(*a)) // Func428(*a, **{
'sid': 32504 })), 0, -1, None)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func208(*a) + Func404(*a)),
'b': int(Func428(*a, **{
'sid': 32504 })) })))
        else:
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckPerformCodeTime(oTarget, oEventCB, 1312) == 0 or cl_evcon.CheckHasState(oTarget, oEventCB, 32547):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, (lambda *a: (Func208(*a) + Func404(*a)) // Func428(*a, **{
'sid': 32504 })), 0, -1, None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
                cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func208(*a) + Func404(*a)),
'b': int(Func428(*a, **{
'sid': 32504 })) })))
            else:
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1312, 1, None):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.CheckPerformCodeTime(oTarget, oEventCB, 1312) == 0 or cl_evcon.CheckHasState(oTarget, oEventCB, 32547):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 32505, (lambda *a: (Func215(*a) + Func404(*a)) // Func428(*a, **{
'sid': 32504 })), 0, -1, None)
            if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32505, None, None) != cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32505 }))):
                cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func215(*a) + Func404(*a)),
'b': int(Func428(*a, **{
'sid': 32504 })) })))
            else:
                cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32504
    m_Name = '#NT#剑心叠层'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
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
        4: CallBack4,
        5: CallBack5,
        6: CallBack6 }

