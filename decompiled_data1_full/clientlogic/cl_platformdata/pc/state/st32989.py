# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32989.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32989.pyc
# Source Generated with Decompyle++
# File: st32989.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func304, Func418, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0)
    cl_action.StateListenAttackerMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 4)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func418(*a)), 'totaldamage')
    cl_evact.RepeatTriggerGroup(oTarget, oEventCB, 1, 2, None)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }))) <= cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'totaldamage' }) * 2)):
        if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32991):
            cl_evact.EventCBAddTargetStateTime(oTarget, oEventCB, 32991, -2000, 4000)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'HPMax' }) / 2 - Func304(*a, **{
'sAttr': 'ArmorMax' }) / 2 - Func304(*a, **{
'sAttr': 'ShieldMax' }) / 2), 'totaldamage')
        else:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32990, 400, { }, None)
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32991, 4000, { }, None)
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'checkrange' })), WARRIOR_MONSTER, 1, 1, 0, 0, 0, None, None)
            cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 3)
            cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: -Func304(*a, **{
'sAttr': 'HPMax' }) / 2 - Func304(*a, **{
'sAttr': 'ArmorMax' }) / 2 - Func304(*a, **{
'sAttr': 'ShieldMax' }) / 2), 'totaldamage')


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBUsePerform(oTarget, oEventCB, 1914, 0, { })


def CallBack4(oEventCB, oTarget):
    if cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1301002) or cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1403003) or cl_condition.CheckCurLevel(oTarget, oEventCB.GetCBLifeCycle(), 1403004):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'checkrange', 40)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'checkrange', 15)


class CState(cl_state.CState):
    m_SID = 32989
    m_Name = '#NT#阴阳激耀统计伤害'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
        3: CallBack3,
        4: CallBack4 }

