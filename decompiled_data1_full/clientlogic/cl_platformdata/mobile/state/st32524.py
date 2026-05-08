# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32524.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32524.pyc
# Source Generated with Decompyle++
# File: st32524.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, MAGIC_WAND_DAMAGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_SERVANT
from cl_newformula import Func429, Func598

def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if not cl_evcon.EventCBCheckVictimForSelf(oTarget, oEventCB) or cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERSISTENCE) or cl_evcon.CheckTargetIsSelfSummon(oTarget, oEventCB, WARRIOR_SERVANT):
        cl_evact.EventCBDoneEvent(oTarget, oEventCB, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL)
        cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) * Func429(*a, **{
'sArg': 'CoastRatio' }) / 10000), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, MAGIC_WAND_DAMAGE, 0, None)
        cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'w1010_Dam', (lambda *a: -(Func598(*a, **{
'sKey': 'w1010_Dam' }) * Func429(*a, **{
'sArg': 'CoastRatio' }) / 10000)), 1)
        cl_evact.EventCBSetWandCount(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'w1010_Dam' }) // 100))


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


class CState(cl_state.CState):
    m_SID = 32524
    m_Name = '伤害附加'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        1: CallBack1 }

