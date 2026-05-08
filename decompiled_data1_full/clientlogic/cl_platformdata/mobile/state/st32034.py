# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32034.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32034.pyc
# Source Generated with Decompyle++
# File: st32034.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_OVERTIME, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 15 / 100 + 0)):
        cl_action.StateAddState(oTarget, oLifeCycle, 1060, 300, { }, None)
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateAddSelfCountByFinalDamage(oTarget, oEventCB, 100, 1)


class CState(cl_state.CState):
    m_SID = 32034
    m_Name = '#NT#千钧一发'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_OVERTIME
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

