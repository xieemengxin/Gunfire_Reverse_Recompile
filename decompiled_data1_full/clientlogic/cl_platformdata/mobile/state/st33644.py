# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33644.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33644.pyc
# Source Generated with Decompyle++
# File: st33644.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EQUIP_MASK_WEAPON, EXTGRADE_GROUP3, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_ITEMBASEGRADE_BEFORE, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oLifeCycle, EXTGRADE_GROUP3, (lambda *a: Func404(*a)), 0, 1)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP3, (lambda *a: Func404(*a)), 0, 1)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.EventCBCheckItemType(oTarget, oEventCB, EQUIP_MASK_WEAPON):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ChangeGrade' })), None)
        cl_evact.EventCBAddMessageInfo(oTarget, oEventCB, 'GradeTransfer', 1)
        cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33644
    m_Name = '技术娴熟行者场外天赋效果'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

