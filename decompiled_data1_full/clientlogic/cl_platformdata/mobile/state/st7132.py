# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7132.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7132.pyc
# Source Generated with Decompyle++
# File: st7132.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBTriggerDropBullet(oTarget, oEventCB, {
        4502: 90,
        4503: 25,
        4504: 8 }, {
        4502: 10,
        4503: 10,
        4504: 10 }, 2, 0, {
        'angle': 90,
        'random': 3,
        'min': 2 })
    cl_evact.CBTriggerGroup(oTarget, oEventCB, {
        1: 5000 }, None)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBTriggerDropBullet(oTarget, oEventCB, {
        4508: 1 }, {
        4508: 10 }, 1, 0, {
        'angle': 90,
        'random': 3,
        'min': 2 })


class CState(cl_state.CState):
    m_SID = 7132
    m_Name = '#NT#精英狙击怪分身掉子弹'
    m_DieRemove = 1
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

