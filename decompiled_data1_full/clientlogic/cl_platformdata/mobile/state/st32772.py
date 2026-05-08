# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32772.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32772.pyc
# Source Generated with Decompyle++
# File: st32772.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT, OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func331, Func336, Func404, Func535

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, -1, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateStatistics(oTarget, oEventCB, 32772, 'NoConsume'):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'NoConsume')
        cl_evact.EventReduceBulletUse(oTarget, oEventCB, 1011)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'CardCnt' })), None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func404(*a) // (10 - (Func331(*a, **{
'sid': 3206 }) - 1) * 2)), 'NoConsume')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func404(*a)),
'b': int(10 - (Func331(*a, **{
'sid': 3206 }) - 1) * 2) })))
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'CardCnt' })), None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func404(*a) // (10 - (Func331(*a, **{
'sid': 3206 }) - 1) * 2)), 'NoConsume')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func3(*a, **{
'a': int(Func404(*a)),
'b': int(10 - (Func331(*a, **{
'sid': 3206 }) - 1) * 2) })))


def CallBack3(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func535(*a))) > 0 and cl_evcon.CheckHasState(oTarget, oEventCB, 32773) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32773, 500, 1, { }, -1, None, None)
        cl_action.CommonAppendQuality(oTarget, oEventCB.GetCBLifeCycle(), 0, GAMBLER_CHOOSE_EQUITY, 0, 1, GAMBLER_REPLACE_DEFAULT, None)


class CState(cl_state.CState):
    m_SID = 32772
    m_Name = '#NT#赌侠Q6觉醒lv3'
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
        3: CallBack3 }

