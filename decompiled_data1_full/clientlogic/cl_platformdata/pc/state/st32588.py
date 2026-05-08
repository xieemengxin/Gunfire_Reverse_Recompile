# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32588.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32588.pyc
# Source Generated with Decompyle++
# File: st32588.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction32587 as CustomAction
import cl_state
from cl_commondefines import OBJ_SELF, OBJ_VICTIM, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_NORMAL, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST32587-NORMAL', cl_evact.EventGetTargetNum(oTarget, oEventCB))
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_ELITE, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST32587-ELITE', cl_evact.EventGetTargetNum(oTarget, oEventCB))
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_BOSS, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'ST32587-BOSS', cl_evact.EventGetTargetNum(oTarget, oEventCB))
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5419) == 1:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.95,
            'Elite': 0.9,
            'Boss': 0.85,
            'Count': 1 }))
    elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5419) == 2:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.9,
            'Elite': 0.8,
            'Boss': 0.7,
            'Count': 1 }))
    else:
        cl_evact.StateSetSelfCount(oTarget, oEventCB, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.85,
            'Elite': 0.7,
            'Boss': 0.55,
            'Count': 1 }))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5419) == 1:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.95,
            'Elite': 0.9,
            'Boss': 0.85 }), 0, '')
    elif cl_evcon.CheckTalentLevel(oTarget, oEventCB, 5419) == 2:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.9,
            'Elite': 0.8,
            'Boss': 0.7 }), 0, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_VICTIM, 0, CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'Normal': 0.85,
            'Elite': 0.7,
            'Boss': 0.55 }), 0, '')


class CState(cl_state.CState):
    m_SID = 32588
    m_Name = '固若金汤'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

