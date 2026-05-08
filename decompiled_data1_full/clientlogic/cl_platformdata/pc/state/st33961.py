# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33961.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33961.pyc
# Source Generated with Decompyle++
# File: st33961.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_action.CommonDeductWeaponBagBulletByWeight(oTarget, oEventCB.GetCBLifeCycle(), cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), {
            4502: 6,
            4503: 3,
            4504: 1 }, None, 1)
        if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ProbCrazyEff') * Func404(*a))) and cl_evcon.CheckAttackInShield(oTarget, oEventCB) == 0:
            cl_evact.EventCBAddCollectInfo(oTarget, oEventCB, 'st33961', 1, 0)
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack2(oEventCB, oTarget):
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCrazyEff')), 0, MAIN_HOLD)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCrazyEff')),
        'cdrate': (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ProbCrazyEff')) })


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCrazyEff')), 0, MAIN_HOLD)
    cl_action.StateRefreshStateExtraInfo(oTarget, oEventCB.GetCBLifeCycle(), {
        'ExcessiveDam': (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('AddCrazyEff')),
        'cdrate': (lambda *a: Func404(*a) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ProbCrazyEff')) })
    cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'CrazyEff', 0, 0, -1)


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'st33961', 0):
        cl_evact.EventCBSetDamageType(oTarget, oEventCB, DAM_TYPE_WEAKNESS)


class CState(cl_state.CState):
    m_SID = 33961
    m_Name = '武器-低频暴击'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 20,
        'firsttime': 20 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

