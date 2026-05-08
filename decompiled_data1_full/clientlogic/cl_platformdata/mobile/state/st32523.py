# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32523.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32523.pyc
# Source Generated with Decompyle++
# File: st32523.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func354, Func369, Func402, Func437, Func610

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 6, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 32523, (lambda *a: Func610(*a, **{
'iStateSID': 33011,
'sKey': 'ExcessiveDam' })), 'ExcessiveDam')


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33011, (lambda *a: Func437(*a, **{
'sKey': 'ExcessiveDam' })), 'ExcessiveDam')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1911, 1, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'EffectMainTarget', 0) == 0:
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'EffectMainTarget', 1)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') * 5 // 10, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') * -5 // 10, 'ExcessiveDam')


def CallBack2(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if not cl_evcon.CheckTargetHasState(oTarget, oEventCB, 7952, 0, 0, 0, 0) or cl_evcon.CheckTargetHasState(oTarget, oEventCB, 1206, 0, 0, 0, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func354(*a) * (Func402(*a) * 0.1 + 0.3)), 'ExcessiveDam')
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1914, 1, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func369(*a) * Func402(*a) * 0.5), 'ExcessiveDam')


def CallBack4(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ST32523_Old'):
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') // 100 }, 32523)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST32523_Old', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'))


def CallBack6(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') // 100 }, 32523)


class CState(cl_state.CState):
    m_SID = 32523
    m_Name = '蕴雷秘法'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        1: CallBack1,
        2: CallBack2,
        4: CallBack4,
        6: CallBack6 }

