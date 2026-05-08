# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33933.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33933.pyc
# Source Generated with Decompyle++
# File: st33933.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func340

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonRecordMoveDis(oTarget, oLifeCycle, '33933')


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBRecordMoveDis(oTarget, oEventCB, '33933', OBJECT_OWNER, 0)
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 33933 }))) <= 1:
        cl_evact.StateCBUsePerform(oTarget, oEventCB, 7355, 0, { }, 0)
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, '33933', OBJECT_OWNER, 0, 0)


class CState(cl_state.CState):
    m_SID = 33933
    m_Name = '#NT#第六赛季自爆妖灵位置检查'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 350,
        'firsttime': 350 }
    m_CBFuncAction = {
        0: CallBack0 }

