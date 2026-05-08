# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st7946.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st7946.pyc
# Source Generated with Decompyle++
# File: st7946.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MG_CASH, MG_EQUIP, MG_RELIC, MG_TRIGGER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0 or cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_CASH):
        cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
    elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 1:
        if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_CASH):
            cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
        if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_TRIGGER):
            cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
        elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 2:
            if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_CASH):
                cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
            if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_TRIGGER):
                cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
            if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_EQUIP):
                cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
            elif cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 3:
                if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_CASH):
                    cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
                if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_TRIGGER):
                    cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
                if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_EQUIP):
                    cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)
                if cl_evcon.CheckMiniGameType(oTarget, oEventCB, MG_RELIC):
                    cl_evact.EventCBChangeMiniGameTimesCal(oTarget, oEventCB, 0, 10000, 0, 0)


class CState(cl_state.CState):
    m_SID = 7946
    m_Name = '#NT#宝箱怪计数结算'
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

