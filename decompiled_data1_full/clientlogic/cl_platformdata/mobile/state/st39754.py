# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st39754.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st39754.pyc
# Source Generated with Decompyle++
# File: st39754.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_PET

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 5000, 0, 0, 1)
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', 5000, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckTargetFightType(oTarget, oEventCB.GetCBLifeCycle(), WARRIOR_PET):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', -6600, 0, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'AttSpeed', 30000, 0, 0)


class CState(cl_state.CState):
    m_SID = 39754
    m_Name = '#NT#召唤法杖狂暴状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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

