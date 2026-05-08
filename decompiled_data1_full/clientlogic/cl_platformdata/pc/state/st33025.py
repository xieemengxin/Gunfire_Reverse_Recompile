# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33025.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33025.pyc
# Source Generated with Decompyle++
# File: st33025.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, BOX_DOUBLE_DAMAGE, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func373, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 12020, 0, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'TotalHP', (lambda *a: cl_evcon.GetTargetTotalAllHP(oTarget, oEventCB) * (0.5 + Func373(*a, **{
'sid': 50009 }) * 0.5)))
        if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORMAL):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'TotalHP' }) * 7.5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, BOX_DOUBLE_DAMAGE, None, None)
        elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'TotalHP' }) * 3.5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, BOX_DOUBLE_DAMAGE, None, None)
        elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_BOSS):
            cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'TotalHP' }) * 1.5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, BOX_DOUBLE_DAMAGE, None, None)


class CState(cl_state.CState):
    m_SID = 33025
    m_Name = '#NT#元素灵胚剑气真伤'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

