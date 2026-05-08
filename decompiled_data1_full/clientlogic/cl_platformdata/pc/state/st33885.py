# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33885.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33885.pyc
# Source Generated with Decompyle++
# File: st33885.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckSceneFightMonster(oTarget, oEventCB.GetCBLifeCycle()) or cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'IsFighting') == 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsFighting', 1)
        cl_action.CommonSendStateStartMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, 0)
    elif cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'IsFighting') == 1:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'IsFighting', 0)
        cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 1, { })


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def StateRefreshAction(oTarget, oLifeCycle):
    if not cl_condition.CommonCheckStateArgsDict(oTarget, oLifeCycle, 33885, 'EnableCount', 0, 0):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


class CState(cl_state.CState):
    m_SID = 33885
    m_Name = '#NT#通用检测交战状态'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

