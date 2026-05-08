# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33402.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33402.pyc
# Source Generated with Decompyle++
# File: st33402.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33402 as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, EQUIP_LASER, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }))) == 1:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'AbnormalSourceDam' }))) == 2:
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func429(*a, **{
'sArg': 'TalentLevel' }) + Func429(*a, **{
'sArg': 'Cache' }) * Func429(*a, **{
'sArg': 'Att' })) * Func429(*a, **{
'sArg': 'Att' })), DAM_MASK_ELEMENT, 1, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (Func429(*a, **{
'sArg': 'TalentLevel' }) + Func429(*a, **{
'sArg': 'Cache' }) * Func429(*a, **{
'sArg': 'Att' })) * Func429(*a, **{
'sArg': 'Att' })), 0, DAM_MASK_ELEMENT, '')


def CallBack2(oEventCB, oTarget):
    if not cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, 0, (lambda *a: (Func429(*a, **{
'sArg': 'TalentLevel' }) + Func429(*a, **{
'sArg': 'Cache' }) * Func429(*a, **{
'sArg': 'Att' })) * Func429(*a, **{
'sArg': 'Att' })), DAM_MASK_ELEMENT, 1, 0)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER):
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: (Func429(*a, **{
'sArg': 'TalentLevel' }) + Func429(*a, **{
'sArg': 'Cache' }) * Func429(*a, **{
'sArg': 'Att' })) * Func429(*a, **{
'sArg': 'Att' })), 0, DAM_MASK_ELEMENT, '')


class CState(cl_state.CState):
    m_SID = 33402
    m_Name = '#隐身套装增益-技能额外增伤'
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
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

