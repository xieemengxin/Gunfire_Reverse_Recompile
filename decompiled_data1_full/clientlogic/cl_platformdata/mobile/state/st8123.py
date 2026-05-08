# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8123.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8123.pyc
# Source Generated with Decompyle++
# File: st8123.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_only import PY_FLAG_EXCLUDEHATE
from cl_newformula import Func404, Func518

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonForbidSpawnFlaw(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEHATE, 1)
    cl_evact.EventChangeHP(oTarget, oEventCB, 1)
    cl_evact.EventCBSetTargetConquerStatus(oTarget, oEventCB, 2)
    cl_action.CommonAddSpecialKey(oTarget, oEventCB.GetCBLifeCycle(), FIGHT_KEY_WUDI, 0)
    cl_action.CommonWalkToGround(oTarget, oEventCB.GetCBLifeCycle())
    cl_action.CommonSetImmobilize(oTarget, oEventCB.GetCBLifeCycle())


def CallBack1(oEventCB, oTarget):
    cl_action.CommonSetPyFlag(oTarget, oEventCB.GetCBLifeCycle(), PY_FLAG_EXCLUDEHATE, 0)
    cl_evact.EventCBSetTargetConquerStatus(oTarget, oEventCB, 1)
    if not cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func518(*a, **{
'sAttr': 'FinishConquerNoRecover' }))):
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 8124, 150, { }, (lambda *a: Func404(*a)))


class CState(cl_state.CState):
    m_SID = 8123
    m_Name = '#NT#妖化怪-虚弱'
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

