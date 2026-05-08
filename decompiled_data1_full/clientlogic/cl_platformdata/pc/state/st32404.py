# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32404.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32404.pyc
# Source Generated with Decompyle++
# File: st32404.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', -4000, 0, None)
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, 4000, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StatusEffect' }))) > 0:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 2000, 0, -1)
        cl_action.CommonListenLevelCtrlMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_LEVEL_ROOMGOAL, -1, 1)


def CallBack0(oEventCB, oTarget):
    cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, 4000, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 500, 9000)


class CState(cl_state.CState):
    m_SID = 32404
    m_Name = '争分夺秒'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

