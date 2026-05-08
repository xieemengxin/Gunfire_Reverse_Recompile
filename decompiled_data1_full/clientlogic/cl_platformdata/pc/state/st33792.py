# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33792.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33792.pyc
# Source Generated with Decompyle++
# File: st33792.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DICE_SUBMSG_ADD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func802

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetDiceAnchoringPoint(oTarget, oLifeCycle, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func802(*a)))
    cl_action.CommonSetDiceAnchoringPoint(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: min(10, 1 + Func404(*a) // 50)))
    cl_evact.StateRefreshCountToClinet(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33792
    m_Name = '运涨骰高'
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
        0: CallBack0 }

