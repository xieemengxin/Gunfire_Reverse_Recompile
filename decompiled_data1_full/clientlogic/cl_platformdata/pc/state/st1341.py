# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1341.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1341.pyc
# Source Generated with Decompyle++
# File: st1341.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func336

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 0, 1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCheckFromSameItem(oTarget, oEventCB):
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'ChargeLevel' }))) > 7:
            cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'CrazyEff', (lambda *a: Func336(*a, **{
'sKey': 'ChargeLevel' }) * 1500), 0)
            cl_evact.EventChangeSkillCache(oTarget, oEventCB, 'Att', 0, (lambda *a: Func336(*a, **{
'sKey': 'ChargeLevel' }) * 1000))
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 1341
    m_Name = '#NT#暴击倍率增加'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

