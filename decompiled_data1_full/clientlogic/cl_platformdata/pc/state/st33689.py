# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33689.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33689.pyc
# Source Generated with Decompyle++
# File: st33689.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, MAGIC_WAND_DAMAGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_SERVANT
from cl_newformula import Func354, Func369, Func598

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 5, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if not cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERFORM) and cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 51323, 0, 0) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'SpillDam', (lambda *a: Func369(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Damage') / 100), 1)
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func354(*a))) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange'):
            cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'SpillDam', (lambda *a: Func354(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange') / 100), 1)
            cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)
        else:
            cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)
    elif cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func354(*a))) and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange'):
        cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'SpillDam', (lambda *a: Func354(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange') / 100), 1)
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)
    else:
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)


def CallBack2(oEventCB, oTarget):
    if cl_condition.StateCheckLiteCDInColdTime(oTarget, oEventCB.GetCBLifeCycle()) == 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        if not cl_evcon.EventCBCheckVictimForSelf(oTarget, oEventCB) or cl_evcon.CheckSrcDamType(oTarget, oEventCB, DAM_TYPE_PERSISTENCE) or cl_evcon.CheckTargetIsSelfSummon(oTarget, oEventCB, WARRIOR_SERVANT):
            cl_action.StateSetLiteCD(oTarget, oEventCB.GetCBLifeCycle(), 100)
            if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExcessChange'):
                cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) * 20 / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, MAGIC_WAND_DAMAGE, 0, None)
                cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'SpillDam', (lambda *a: -Func598(*a, **{
'sKey': 'SpillDam' }) * 20 / 100), 1)
                cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                    'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)
            else:
                cl_evact.EventTargetDamage(oTarget, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) * 20 / 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 1, 0, 0, 1, 0, 0, MAGIC_WAND_DAMAGE, 0, None)
                cl_evact.EventCBAddSavedData(oTarget, oEventCB, 'SpillDam', (lambda *a: -Func598(*a, **{
'sKey': 'SpillDam' }) * 20 / 100), 1)
                cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
                    'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)


def CallBack5(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func598(*a, **{
'sKey': 'SpillDam' }) // 100) }, 33689)


class CState(cl_state.CState):
    m_SID = 33689
    m_Name = '主要技能-储灵打击'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        5: CallBack5 }

