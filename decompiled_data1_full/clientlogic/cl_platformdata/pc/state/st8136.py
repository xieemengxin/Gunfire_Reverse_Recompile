# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8136.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8136.pyc
# Source Generated with Decompyle++
# File: st8136.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_USE_HP, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func361, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 2, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 8136, (lambda *a: Func361(*a, **{
'sid': 14415,
'sArgs': 'PF39247_Shield_Cure_Max' })), 'Percentage')


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 39247, 1, 0):
        if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }))):
            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * Func437(*a, **{
'sKey': 'Percentage' }) / 1000), 0, DAM_USE_SHIELD)
        else:
            cl_action.StateCureByAtive(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * Func437(*a, **{
'sKey': 'Percentage' }) / 1000), 0, DAM_USE_HP)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 39247, 1, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'SkillNum')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SkillNum') >= 2:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'Percentage', (lambda *a: max(int(Func361(*a, **{
'sid': 14415,
'sArgs': 'PF39247_Shield_Cure_Min' })), int(Func437(*a, **{
'sKey': 'Percentage' }) - Func361(*a, **{
'sid': 14415,
'sArgs': 'PF39247_Shield_Cure_Decrease' })))))


class CState(cl_state.CState):
    m_SID = 8136
    m_Name = '#NT#轮回10妖王强化-护盾恢复'
    m_IsShow = 1
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
        2: CallBack2 }

