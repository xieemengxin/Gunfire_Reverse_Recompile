# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8164.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8164.pyc
# Source Generated with Decompyle++
# File: st8164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MUTANT_NUM_CHANGE, OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func738

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenLevelCtrlMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_LEVEL_COMMON_ROOMCHALLENGE, MUTANT_NUM_CHANGE, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'MutantNum' }))) >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func738(*a, **{
'sKey': 'MutantLimit' }))):
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1)
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, -2500, 0, '')


class CState(cl_state.CState):
    m_SID = 8164
    m_Name = '#NT#异化怪特效'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
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

