# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32815.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32815.pyc
# Source Generated with Decompyle++
# File: st32815.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func331, Func360, Func361

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_BLOCK, -1, 1, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1696, {
        'PerformAtt': (lambda *a: Func360(*a, **{
'sid': 1310,
'sAttr': 'Att' })),
        'Radius': (lambda *a: Func361(*a, **{
'sid': 2902,
'sArgs': 'Radius' })) }, None)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: 25 + Func331(*a, **{
'sid': 2902 }) * 25)):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_evact.EventCBUsePerformEvtTarget(oTarget, oEventCB, 1696, {
            'PerformAtt': (lambda *a: Func360(*a, **{
'sid': 1310,
'sAttr': 'Att' })),
            'Radius': (lambda *a: Func361(*a, **{
'sid': 2902,
'sArgs': 'Radius' })) }, None)


class CState(cl_state.CState):
    m_SID = 32815
    m_Name = '#NT#反击之潮'
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
        'delay': (lambda *a: 140 - Func331(*a, **{
'sid': 2902 }) * 20) }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

