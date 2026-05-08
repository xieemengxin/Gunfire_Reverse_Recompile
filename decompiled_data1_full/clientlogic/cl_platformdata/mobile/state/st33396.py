# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33396.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33396.pyc
# Source Generated with Decompyle++
# File: st33396.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MAIN_HOLD, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func555

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeEnergy(oTarget, oEventCB.GetCBLifeCycle(), 200, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'DebuffProb', 0, 5000)
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'SkillDebuffProb': cl_action.CommonGetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1423, 'DebuffProb') // 100,
        'WeaponDebuffProb': (lambda *a: Func555(*a, **{
'sAttr': 'DebuffProb' }) // 100) }, 33396)


def CallBack2(oEventCB, oTarget):
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1423, 'DebuffProb', 5000, 0)
    cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 8007, 'DebuffProb', 5000, 0)
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DebuffProb', 0, 5000, MAIN_HOLD)


def CallBack3(oEventCB, oTarget):
    cl_action.CommonRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'SkillDebuffProb': cl_action.CommonGetPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1423, 'DebuffProb') // 100,
        'WeaponDebuffProb': (lambda *a: Func555(*a, **{
'sAttr': 'DebuffProb' }) // 100) }, 33396)


def CallBack4(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponAttr(oTarget, oEventCB, 'DebuffProb', 0, 0)


class CState(cl_state.CState):
    m_SID = 33396
    m_Name = '#NT#璃3117天赋状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

