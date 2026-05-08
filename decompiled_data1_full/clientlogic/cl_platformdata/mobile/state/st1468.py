# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1468.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1468.pyc
# Source Generated with Decompyle++
# File: st1468.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, SKILLCACHE_PARENTACTNUM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, 5000, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, None, { })


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1313, 1, None) and cl_evcon.CheckStateStatistics(oTarget, oEventCB, 1468, 'ParentActnum') == cl_evcon.EventCBCheckSkillCache(oTarget, oEventCB, SKILLCACHE_PARENTACTNUM):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) == 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1468
    m_Name = '剑术精研'
    m_DieRemove = 1
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
        0: CallBack0 }

