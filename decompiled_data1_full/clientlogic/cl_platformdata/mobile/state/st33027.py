# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33027.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33027.pyc
# Source Generated with Decompyle++
# File: st33027.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33027 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, 1) and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        50005: 1 }, 0, 1) == 0:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, (lambda *a: (Func402(*a) + 2) * 1000), 0, '')


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, 1) and cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        50005: 1 }, 0, 1) == 0:
        CustomAction(oTarget, oEventCB, {
            'ShareCount': (lambda *a: max(Func402(*a) - 1, 1)),
            'Distance': 30,
            'ShareDamageRatio': (lambda *a: (Func402(*a) + 3) * 10),
            'CD': 2,
            'ThunderPlusPF': 1911,
            'MergePF': ((1315, 1709), (12013, 1428), (7153, 13548), (1325,)) })


class CState(cl_state.CState):
    m_SID = 33027
    m_Name = '#NT#金虬银锁怪物伤害传导'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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

