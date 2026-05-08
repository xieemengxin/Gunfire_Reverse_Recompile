# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33139.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33139.pyc
# Source Generated with Decompyle++
# File: st33139.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func598, Func625

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF50223' })))
    cl_action.CommonListenDeviceMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.CBTriggerGroup(oTarget, oEventCB, {
        1: (lambda *a: 200 * Func625(*a)) }, 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)
    cl_action.CommonSetSavedData(oTarget, oEventCB.GetCBLifeCycle(), 'PF50223', (lambda *a: Func598(*a, **{
'sKey': 'PF50223' }) + 1))
    cl_action.CommonChangeUpgradeRelicCnt(oTarget, oEventCB.GetCBLifeCycle(), 1)


class CState(cl_state.CState):
    m_SID = 33139
    m_Name = '英雄核心-紫鸮'
    m_IsShow = 1
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
        0: CallBack0,
        1: CallBack1 }

