# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33241.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33241.pyc
# Source Generated with Decompyle++
# File: st33241.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ENERGY_RS_LICAREER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func538

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeCareerPerformAttr(oTarget, oLifeCycle, 'ColdTime', -10000, 0, None)
    cl_action.CommonSubCareerPerformColdTime(oTarget, oLifeCycle, 0, 100)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM, -1, 1, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 215):
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckChangeEnergyReason(oTarget, oEventCB, ENERGY_RS_LICAREER):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oTarget, oEventCB, (lambda *a: Func538(*a)))


def CallBack1(oEventCB, oTarget):
    cl_action.CommonChangeCareerPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ColdTime', -10000, 0, None)
    cl_action.CommonSubCareerPerformColdTime(oTarget, oEventCB.GetCBLifeCycle(), 0, 100)


class CState(cl_state.CState):
    m_SID = 33241
    m_Name = '#NT#词条50684'
    m_DieRemove = 1
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

