# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33724.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33724.pyc
# Source Generated with Decompyle++
# File: st33724.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DICE_SUBMSG_DISASSEMBLE, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DICECHANGE, DICE_SUBMSG_DISASSEMBLE, 0, 0, 0)
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func402(*a))) <= 4:
        cl_action.CommonCopyAssembleEffect(oTarget, oLifeCycle, {
            51329: 1 }, 2, 0)
    else:
        cl_action.CommonCopyAssembleEffect(oTarget, oLifeCycle, {
            51329: 1 }, 1, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBDisableLinkCopyAbility(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33724
    m_Name = '#NT#镜像骰子'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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

