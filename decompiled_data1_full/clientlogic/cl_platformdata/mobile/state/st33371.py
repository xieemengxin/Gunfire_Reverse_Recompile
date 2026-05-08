# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33371.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33371.pyc
# Source Generated with Decompyle++
# File: st33371.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_TRUE, OBJ_FRIEND_HERO, OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func304, Func374

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.GetStateStatistics(oTarget, oLifeCycle, 33371, '33371Enable'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.StateReceiveDam(oTarget, oLifeCycle, (lambda *a: min(int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 50 / 100), int(Func374(*a) - 2))), DAM_TYPE_TRUE, 0, 0, 0, 0, None)
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 15)


def CallBack0(oEventCB, oTarget):
    if cl_condition.CheckHasRelic(oTarget, oEventCB.GetCBLifeCycle(), 5964) == 0 or cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33371, '33371Enable') == 0:
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33371, 1, '33371Enable')
    elif cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33371, '33371Enable'):
        cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33371, 0, '33371Enable')
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 15)


def CallBack3(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByTargetType(oTarget, oEventCB, 15, OBJ_FRIEND_HERO, 0)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) == 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    else:
        cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 15)


class CState(cl_state.CState):
    m_SID = 33371
    m_Name = '独木难支'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 15
    m_StartCount = 15
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
        'delay': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        3: CallBack3 }

