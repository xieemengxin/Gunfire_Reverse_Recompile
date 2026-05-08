# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32531.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32531.pyc
# Source Generated with Decompyle++
# File: st32531.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 32341, 0, { }, None)
    cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32340, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if oTarget.HP() > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.4 + cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2401) / 10))):
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 32341, 0)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32340, 0, { }, None)


class CState(cl_state.CState):
    m_SID = 32531
    m_Name = '#NT#狂怒冷却'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

