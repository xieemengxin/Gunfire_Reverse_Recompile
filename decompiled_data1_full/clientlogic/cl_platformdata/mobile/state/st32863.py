# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32863.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32863.pyc
# Source Generated with Decompyle++
# File: st32863.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_THROW, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func336, Func402, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 3, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func331(*a, **{
'sid': 3309 }))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, None)
    else:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1426: 1,
        8009: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st32863', None):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 5000 * Func402(*a) * Func336(*a, **{
'sKey': 'st32863' })), 0, 0, '')
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1426: 1,
        8009: 1 }, 0, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st32863', None):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: 15000 * Func336(*a, **{
'sKey': 'st32863' })), 0, 0, '')
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oTarget, oEventCB, 32863, 10, 0, None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1426: 1,
        8009: 1 }, 0, 0):
        cl_evact.EventCBClearCollectInfo(oTarget, oEventCB, 'st32863', None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB):
            cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'st32863', (lambda *a: Func404(*a)))
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32863
    m_Name = '疾风骤雨'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

