# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33349.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33349.pyc
# Source Generated with Decompyle++
# File: st33349.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_MAINWEAPON, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5920) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33349, '33349Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33349, 1, '33349Enable')
        cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
        cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', -10000, 0, EQUIP_TYPE_MAINWEAPON)
        cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', -10000, 0, EQUIP_TYPE_FUNDAMENTALWEAPON)
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33349, '33349Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33349, 0, '33349Enable')
        cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1)
        cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', 0, 0, EQUIP_TYPE_MAINWEAPON)
        cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', 0, 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', -10000, 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oTarget, oEventCB, 'CrazyEff', -10000, 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


class CState(cl_state.CState):
    m_SID = 33349
    m_Name = '猫眼瞄具'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

