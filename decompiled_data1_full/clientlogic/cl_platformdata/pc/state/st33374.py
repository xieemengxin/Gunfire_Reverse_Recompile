# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33374.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33374.pyc
# Source Generated with Decompyle++
# File: st33374.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func619

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, min(5, int(cl_action.CommonGetSeasonSuitArg(oTarget, oLifeCycle, 15101, '33374Count', 0))))
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func619(*a, **{
'sAttr': 'TalentLevel' }))) == 1:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 30)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func619(*a, **{
'sAttr': 'TalentLevel' }))) == 2:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 30)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func619(*a, **{
'sAttr': 'TalentLevel' }))) == 3:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 7, 0, 30)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSeasonSuitArg(oTarget, oLifeCycle, 15101, '33374Count', (lambda *a: Func404(*a)), 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckPerformUnCrtByOwner(oTarget, oEventCB):
        cl_evact.EventCBAddDamSign(oTarget, oEventCB, 'st33374', 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBCheckDamSign(oTarget, oEventCB, 'st33374') and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 3000, DAM_TYPE_WEAKNESS, '')


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckHasState(oTarget, oEventCB, 33479):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 3000 * (Func619(*a, **{
'sAttr': 'TalentLevel' }) - 1)), DAM_TYPE_WEAKNESS, '')
    if cl_evcon.EventCBCheckDamSign(oTarget, oEventCB, 'st33374') and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2 and cl_evcon.CheckHasState(oTarget, oEventCB, 33479) == 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33479, 300, { }, None)
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 3000, DAM_TYPE_WEAKNESS, '')


def CallBack7(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_evcon.CheckHasState(oTarget, oEventCB, 33479):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: 3000 * (Func619(*a, **{
'sAttr': 'TalentLevel' }) - 1)), DAM_TYPE_WEAKNESS, '')
    if cl_evcon.EventCBCheckDamSign(oTarget, oEventCB, 'st33374') and cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) >= 2 and cl_evcon.CheckHasState(oTarget, oEventCB, 33479) == 0:
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), -2, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33479, 300, { }, None)
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 6000, DAM_TYPE_WEAKNESS, '')


class CState(cl_state.CState):
    m_SID = 33374
    m_Name = '暴击之眼'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3,
        7: CallBack7 }

