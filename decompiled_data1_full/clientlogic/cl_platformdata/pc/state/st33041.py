# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33041.pyc
# Source Generated with Decompyle++
# File: st33041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33041 as CustomAction
import cl_state
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_FRIEND, OBJ_SELF, STATE_ADD_HIGH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func514, Func518, Func692, Func693

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 2, 0, 0)
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 3, 0, 0)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 1000), 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 9, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 11, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }))) != cl_condition.GetTargetStateInfo(oTarget, oEventCB.GetCBLifeCycle(), 33043, 'TalentLevel'):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33043, 0, { }, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBAddCustomData(oTarget, oEventCB, 'ST33041Dam', (lambda *a: Func693(*a, **{
'sAttr': 'Shield' })))


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBAddCustomData(oTarget, oEventCB, 'ST33041Dam', (lambda *a: Func693(*a, **{
'sAttr': 'Armor' })))


def CallBack5(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'Value': (lambda *a: min(Func518(*a, **{
'sAttr': 'ST33041Dam' }), Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000)) })
    cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


def CallBack6(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'Value': (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000) })
    cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.GetTargetStateNum(oTarget, oEventCB, 33041, 0) == 0:
        cl_action.CommonRemoveState(oTarget, oEventCB.GetCBLifeCycle(), 33043)
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


def CallBack9(oEventCB, oTarget):
    if cl_evcon.CheckTargetAddState(oTarget, oEventCB, 33041):
        cl_evact.EventSetStateStatistics(oTarget, oEventCB, 'HasApply', 1)
        CustomAction(oTarget, oEventCB, {
            'Value': (lambda *a: min(Func518(*a, **{
'sAttr': 'ST33041Dam' }), Func692(*a, **{
'sKey': 'TalentLevel' }) * 5000)) })
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


def CallBack10(oEventCB, oTarget):
    if not cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'HasApply'):
        CustomAction(oTarget, oEventCB, {
            'Value': (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000) })
        cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


def CallBack11(oEventCB, oTarget):
    if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 33043):
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }))) != cl_condition.GetTargetStateInfo(oTarget, oEventCB.GetCBLifeCycle(), 33043, 'TalentLevel'):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33043, 0, { }, 0)
        if not cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'HasApply'):
            CustomAction(oTarget, oEventCB, {
                'Value': (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000) })
            cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)
        else:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33043, 0, { }, 0)
            CustomAction(oTarget, oEventCB, {
                'Value': (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000) })
            cl_evact.EventCBSetCustomData(oTarget, oEventCB, 'ST33041Dam', 0)


class CState(cl_state.CState):
    m_SID = 33041
    m_Name = '寒脉淬体'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_HIGH
    m_TargetType = OBJ_FRIEND
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7,
        9: CallBack9,
        10: CallBack10,
        11: CallBack11 }
    
    def CheckHighAttr(self, oTarget, oOldState):
        if 'arg' not in oOldState.m_StateInfo or 'arg' not in self.m_StateInfo:
            return 0
        iOldStateLevel = oOldState.GetArgValue('TalentLevel', 0)
        iNewStateLevel = self.GetArgValue('TalentLevel', 0)
        return iNewStateLevel > iOldStateLevel


