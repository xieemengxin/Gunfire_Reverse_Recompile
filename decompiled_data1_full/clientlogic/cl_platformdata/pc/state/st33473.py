# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33473.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33473.pyc
# Source Generated with Decompyle++
# File: st33473.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ARMOR, DAM_USE_SHIELD, DEFEND_TREND_ARMOR, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSSDM
from cl_newformula import Func201, Func304, Func341, Func361, Func390, Func391, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonTriggerClientBehavior(oTarget, oLifeCycle, 33473, 3, 0, 0)
    cl_action.CommonSetMaxExcessAttr(oTarget, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' })))
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33473, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 / (20 + 10 * (Func361(*a, **{
'sid': 51007,
'sArgs': 'Count' }) * 1.5 - min(int(Func201(*a)), 4) - 1)) / 30), 'AddShield')
    cl_action.CommonAddPerformArgsValue(oTarget, oLifeCycle, 51007, 'Count', 1, 0)
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_BOSSDM):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_ARMOR) == 0:
        cl_action.CommonAddExcessAttr(oTarget, oLifeCycle, 'Shield', (lambda *a: Func437(*a, **{
'sKey': 'AddShield' })), 0, 1)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
    else:
        cl_action.CommonAddExcessAttr(oTarget, oLifeCycle, 'Armor', (lambda *a: Func437(*a, **{
'sKey': 'AddShield' })), 0, 1)
        cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonRemoveClientBehavior(oTarget, oLifeCycle, 33473)
    if cl_condition.CommonCheckGameReleaseFlag(oTarget, oLifeCycle) == 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 7, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        39153: 1,
        39027: 1,
        39140: 1,
        39141: 1 }, 0, 0):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_END, -1)
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1)
        cl_evact.StateCBSetSelfTime(oTarget, oEventCB, 1200, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func341(*a) % 2)) == 1:
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1)
        cl_evact.StateCBSetSelfTime(oTarget, oEventCB, 1200, 0)


def CallBack3(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func391(*a))) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 30:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 3, 0, 0)


def CallBack5(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 30:
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 6, 0, 0)


def CallBack6(oEventCB, oTarget):
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func390(*a))) <= 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack7(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR) == 0:
        cl_action.CommonChangeDefValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func391(*a)), DAM_USE_SHIELD)
        cl_action.CommonAddExcessAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Shield', (lambda *a: -Func391(*a)), 0, 0)
    else:
        cl_action.CommonChangeDefValue(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: -Func390(*a)), DAM_USE_ARMOR)
        cl_action.CommonAddExcessAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Armor', (lambda *a: -Func390(*a)), 0, 0)


class CState(cl_state.CState):
    m_SID = 33473
    m_Name = '#NT#陆吾遗物回盾'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 10,
        'cnt': 30 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        4: CallBack4,
        5: CallBack5,
        6: CallBack6,
        7: CallBack7 }

