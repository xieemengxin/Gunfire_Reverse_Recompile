# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33729.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33729.pyc
# Source Generated with Decompyle++
# File: st33729.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func410

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonChangeDevicePerformAttr(oTarget, oLifeCycle, 7200, 'EnergyCost', 0, -5000)
    cl_action.CommonChangeDevicePerformAttr(oTarget, oLifeCycle, 7205, 'EnergyCost', 0, -5000)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 33040 }) * 2))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeDeviceAttr(oTarget, oLifeCycle, 'AttSpeed', (lambda *a: Func404(*a) * 100), 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.EventCBCheckFromPointState(oTarget, oEventCB, 33040):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33729
    m_Name = '英雄核心-墨咻'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

