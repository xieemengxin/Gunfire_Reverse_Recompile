# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1101.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1101.pyc
# Source Generated with Decompyle++
# File: st1101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_ELEMENT, OBJ_ATTACK, OBJ_ENEMY, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: min(int(Func404(*a) * 1500 + 0), 7500)), 0, DAM_TYPE_ELEMENT, '')


def CallBack1(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 15, OBJ_ENEMY, 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)


def CallBack2(oEventCB, oTarget):
    if (cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20026, None, None, None, None) or cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20027, None, None, None, None) or cl_evcon.CheckTargetHasState(oTarget, oEventCB, 20028, None, None, None, None)) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) < 5:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


class CState(cl_state.CState):
    m_SID = 1101
    m_Name = '元素汇流'
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
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2 }

