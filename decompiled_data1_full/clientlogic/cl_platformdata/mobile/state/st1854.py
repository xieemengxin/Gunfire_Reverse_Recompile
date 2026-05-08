# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1854.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1854.pyc
# Source Generated with Decompyle++
# File: st1854.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction1854 as CustomAction
import cl_state
from cl_commondefines import FIGHT3_KEY_IGNOREIMMOBILIZE, FIGHT3_KEY_IGNOREUNBALANCE, MOVE_TYPE_JUMP, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func616

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_IGNOREUNBALANCE) or cl_condition.CheckMoveMode(oTarget, oEventCB.GetCBLifeCycle(), MOVE_TYPE_JUMP) or cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_IGNOREIMMOBILIZE):
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), { })
    else:
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), { })
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1864, (lambda *a: Func616(*a)), { }, None)
        cl_action.CommonSendStateStartMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)


def CallBack1(oEventCB, oTarget):
    if not cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_IGNOREUNBALANCE) or cl_condition.CheckMoveMode(oTarget, oEventCB.GetCBLifeCycle(), MOVE_TYPE_JUMP) or cl_evcon.CheckHasLogicKey(oTarget, oEventCB, FIGHT3_KEY_IGNOREIMMOBILIZE):
        cl_action.CommonSetUnbalanceCDStart(oTarget, oEventCB.GetCBLifeCycle())
        cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, { })


class CState(cl_state.CState):
    m_SID = 1854
    m_Name = '#NT#失衡'
    m_DieRemove = 1
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
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

