# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33021.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33021.pyc
# Source Generated with Decompyle++
# File: st33021.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: Func361(*a, **{
'sid': 50002,
'sArgs': 'MoveSpeed' }) * Func404(*a)), 0, -1)
    cl_action.CommonSetStateCount(oTarget, oLifeCycle, 33023, (lambda *a: Func361(*a, **{
'sid': 50002,
'sArgs': 'MoveSpeed' }) * Func404(*a) // 100), None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckInPointPerform(oTarget, oEventCB, {
        1914: 1,
        1911: 1 }, 1, 0):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        if not cl_evcon.CheckHasState(oTarget, oEventCB, 33023):
            cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 33023, 0, { }, 0)
        cl_evact.EventCBAddTargetStateCount(oTarget, oEventCB, 33021, 1, -1, -1, 1000)


class CState(cl_state.CState):
    m_SID = 33021
    m_Name = '#NT#电光火石加成'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 25
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

