# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1789.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1789.pyc
# Source Generated with Decompyle++
# File: st1789.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, MAIN_HOLD, OBJ_ATTACK, OBJ_SELF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_SWITCHWEAPON, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func505, Func525

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 3, 0, 0)
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_SWITCHWEAPON, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 1, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckBulletRatio(oTarget, oEventCB, 51) > 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func525(*a))) > 1:
        cl_evact.EventCBAddHoldWeaponComBullet(oTarget, oEventCB, (lambda *a: min(int(-(Func505(*a) * 10 / 100)), -1)), MAIN_HOLD)
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


def CallBack5(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) * 1000, 0, DAM_TYPE_WEAPON, '')


class CState(cl_state.CState):
    m_SID = 1789
    m_Name = '顺水推舟'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3,
        5: CallBack5 }

