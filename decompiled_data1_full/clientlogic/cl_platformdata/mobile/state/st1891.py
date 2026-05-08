# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1891.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1891.pyc
# Source Generated with Decompyle++
# File: st1891.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDisableWeaponPerform(oTarget, oLifeCycle, 4388)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'AttSpeed', 0, 5000)
    cl_action.CommonStateStatistics(oTarget, oLifeCycle, 1891, 5, 'Limit')


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9017, 1, 0) and cl_evcon.CheckDamageIsSourceWeapon(oTarget, oEventCB):
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= cl_condition.CommonGetWeaponPerformArgs(oTarget, oEventCB.GetCBLifeCycle(), 9093, 'Limit'):
            cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)
            cl_evact.EventCBStartClientSkill(oTarget, oEventCB, 12028, '', 0, None, { })


class CState(cl_state.CState):
    m_SID = 1891
    m_Name = '#NT#追踪步枪吸附'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 5
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

