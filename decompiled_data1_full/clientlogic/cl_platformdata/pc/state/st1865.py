# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1865.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1865.pyc
# Source Generated with Decompyle++
# File: st1865.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckPointRelic(oTarget, oEventCB, 5859):
        if cl_evcon.CheckReason(oTarget, oEventCB, 'npcSelectedRelicCost', 0) or cl_evcon.CheckReason(oTarget, oEventCB, 'FuseSuitCondiReduce', 0) or cl_evcon.CheckReason(oTarget, oEventCB, 'RollRelicPerform', 0):
            cl_evact.EventCBSetSavedData(oTarget, oEventCB, 'UseTalentChooseAll', 0, 0)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1865
    m_Name = '#NT#塞翁失马销毁计数重置'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

