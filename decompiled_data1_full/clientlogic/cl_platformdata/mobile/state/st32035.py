# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32035.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32035.pyc
# Source Generated with Decompyle++
# File: st32035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func311, Func312, Func313, Func331

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 18)


def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.HasState(oTarget, oLifeCycle, 32042):
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 32042, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckDeadlyPredictDam(oTarget, oEventCB, None) and cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventSetLimitDamage(oTarget, oEventCB, (lambda *a: Func311(*a) + Func312(*a) + Func313(*a) - 100))
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32480, 100, { }, None)
        cl_evact.EventChangeHP(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (20 + Func331(*a, **{
'sid': 2032 }) * 10) // 100 + 0))
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
        if cl_evcon.GetTargetStateCount(oTarget, oEventCB, 32035, 1, 0) == 0 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2032) >= 3:
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 32042, 0, { }, None)
        if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) <= 0 and cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2032) < 3:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 32035
    m_Name = '绝处逢生'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 9
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

