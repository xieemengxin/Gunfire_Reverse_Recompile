# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33335.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33335.pyc
# Source Generated with Decompyle++
# File: st33335.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33335 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func619

def CallBack0(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 30:
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Perform': 1939 })
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, (lambda *a: Func619(*a, **{
'sAttr': 'Count' })), None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33335
    m_Name = '#水枪#湿润状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 30
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0 }

