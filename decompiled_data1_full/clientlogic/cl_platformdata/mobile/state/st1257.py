# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1257.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1257.pyc
# Source Generated with Decompyle++
# File: st1257.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_CURSE, QUALITY_TYPE_HIGH, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func210, Func216, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.GetRelicNumByQuality(oTarget, oEventCB, QUALITY_TYPE_HIGH) >= cl_evcon.GetRelicNumByQuality(oTarget, oEventCB, QUALITY_TYPE_CURSE):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func216(*a) - Func210(*a)))
    else:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func210(*a) - Func216(*a)))


def CallBack1(oEventCB, oTarget):
    cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'LuckyHit', (lambda *a: 40 * Func404(*a)), 0)


class CState(cl_state.CState):
    m_SID = 1257
    m_Name = '祸福难料'
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
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

