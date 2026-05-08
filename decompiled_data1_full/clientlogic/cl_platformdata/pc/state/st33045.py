# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33045.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33045.pyc
# Source Generated with Decompyle++
# File: st33045.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, UNBALANCE_WEAPON, WARRIOR_MONSTER
from cl_newformula import Func402, Func437, Func444, Func610

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 3, 0, 0)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33045, (lambda *a: Func610(*a, **{
'iStateSID': 33046,
'sKey': 'ExcessiveDam' })), 'ExcessiveDam')
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEUNBALANCE, UNBALANCE_WEAPON, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33046, (lambda *a: Func437(*a, **{
'sKey': 'ExcessiveDam' })), 'ExcessiveDam')


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckHitFlaw(oTarget, oEventCB) and cl_evcon.CheckFromWeapon(oTarget, oEventCB, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func444(*a) * Func402(*a) * 0.1), 'ExcessiveDam')


def CallBack2(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') != cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ST32523_Old'):
        cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
            'ExcessiveDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') // 100 }, 33045)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST33045_Old', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'))


def CallBack3(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam') // 100 }, 33045)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 3509) == 3 or cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 5, WARRIOR_MONSTER, 0, 0, 0, 0, -1, 0, None)
        cl_evact.EventTargetDamage(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam', 0)
    elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam'), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, -1, 1, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ExcessiveDam', 0)


class CState(cl_state.CState):
    m_SID = 33045
    m_Name = '寒霜凝蕴'
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
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

