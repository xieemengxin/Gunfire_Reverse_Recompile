# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39684.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39684.pyc
# Source Generated with Decompyle++
# File: st39684.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import EXTGRADE_GROUP2, MAIN_HOLD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_COUNT_MAX, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeStateAttr(oTarget, oLifeCycle, 0, oLifeCycle.m_Owner.GetArgValue('MaxCount'), STATE_COUNT_MAX, 1)
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 39684, oLifeCycle.m_Owner.GetArgValue('StateCount'), 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponExtGrade(oTarget, oEventCB.GetCBLifeCycle(), EXTGRADE_GROUP2, (lambda *a: Func404(*a)), MAIN_HOLD, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBClearExtGrade(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 39684
    m_Name = '#NT#S7等级增幅组件'
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

