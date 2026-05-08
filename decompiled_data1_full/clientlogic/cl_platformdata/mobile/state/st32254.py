# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32254.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32254.pyc
# Source Generated with Decompyle++
# File: st32254.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func404(*a) * 2000), None)
    cl_action.CommonModifyDamResistance(oTarget, oLifeCycle, (lambda *a: 2000 * Func404(*a)), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckDamFromSelf(oTarget, oEventCB, None) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)


class CState(cl_state.CState):
    m_SID = 32254
    m_Name = '护法雷衣'
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
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

