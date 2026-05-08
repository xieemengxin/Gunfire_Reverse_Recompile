# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1628.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1628.pyc
# Source Generated with Decompyle++
# File: st1628.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func302

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckHitWeakness(oTarget, oEventCB, 0):
        if cl_evcon.CheckVictimFightType(oTarget, oEventCB, WARRIOR_ELITE) or cl_evcon.GetVictimHPRatio(oTarget, oEventCB) <= 40:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, None, None, None, None, None, None)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 5, WARRIOR_NORMAL, 0, 0, 0, 0, -1, None, None)
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * 10), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, -1, -1, -1, None, None, None)
        else:
            cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, None, None, None, None, None, None)
            cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 5, WARRIOR_NORMAL, 1, 0, 0, 0, -1, None, None)
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * 10), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 1, 0, 0, 0, -1, -1, -1, None, None, None)


class CState(cl_state.CState):
    m_SID = 1628
    m_Name = '#NT#弱点射击'
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
        0: CallBack0 }

