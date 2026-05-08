# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1744.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1744.pyc
# Source Generated with Decompyle++
# File: st1744.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EXTGRADE_GROUP2, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREPLACEWEAPON, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP2, (lambda *a: -Func404(*a)), 0, None)
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP2, (lambda *a: -Func404(*a)), -1, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, (lambda *a: -Func404(*a)))


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBChangeWeaponExtGrade(oTarget, oEventCB, EXTGRADE_GROUP2, 0)


class CState(cl_state.CState):
    m_SID = 1744
    m_Name = '幕后交易（怪物）'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 8
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

