# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33616.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33616.pyc
# Source Generated with Decompyle++
# File: st33616.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, TRIGGER_PARASITIC
from cl_newformula import Func651

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PARASITIC, TRIGGER_PARASITIC, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BaseProbability') + Func651(*a, **{
'sKey': 'ParasiticCount' }) * oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('ExtraProbability'))):
        if cl_evcon.CheckTargetHasState(oTarget, oEventCB, 33867, 0, 0, 0, 0):
            cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33867, 1, 0, 0, 0)
        else:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 33867, 0, 0, {
                'MaxCnt': 10,
                'AddDamFactor': 10,
                'SlowFactor': 10 }, 1, 0, 1)


class CState(cl_state.CState):
    m_SID = 33616
    m_Name = '#NT#园丁Q4'
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
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

