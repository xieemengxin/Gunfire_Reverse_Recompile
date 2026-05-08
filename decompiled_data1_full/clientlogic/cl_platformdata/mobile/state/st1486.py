# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1486.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1486.pyc
# Source Generated with Decompyle++
# File: st1486.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func307

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func307(*a))) < 1:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_condition.GetRelicGrade(oTarget, oEventCB.GetCBLifeCycle(), 5775) == 1:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1485, 0, { }, None)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1803, 0, { }, None)
    elif cl_condition.GetRelicGrade(oTarget, oEventCB.GetCBLifeCycle(), 5775) == 2:
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1802, 0, { }, None)


class CState(cl_state.CState):
    m_SID = 1486
    m_Name = '#NT#复原灵龛受伤计时'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 4,
        'firsttime': 500,
        'cnt': 1 }
    m_CBFuncAction = {
        0: CallBack0 }

