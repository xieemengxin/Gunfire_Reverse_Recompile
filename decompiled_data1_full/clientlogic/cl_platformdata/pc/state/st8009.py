# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8009.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8009.pyc
# Source Generated with Decompyle++
# File: st8009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventChangeEnergy(oTarget, oEventCB, 30000)
    cl_evact.EventGetHeroTarget(oTarget, oEventCB, 0, 1, 0, None)
    cl_evact.EventCBEnableTargetBulletChangeRule(oTarget, oEventCB, 11109, 1)
    cl_evact.StateCBAddVictimState(oTarget, oEventCB, 8014, 0, 1, { }, -1, None, None)


class CState(cl_state.CState):
    m_SID = 8009
    m_Name = '#NT#妖王逆散前摇回满能量'
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
        0: CallBack0 }

