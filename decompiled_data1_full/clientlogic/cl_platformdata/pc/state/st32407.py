# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32407.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32407.pyc
# Source Generated with Decompyle++
# File: st32407.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_OWNER, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func223, Func340, Func597

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBRecordMoveDis(oTarget, oEventCB, 'st32407', OBJECT_OWNER, 0)
    if cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func340(*a, **{
'sKey': 'st32407' }))) >= 10:
        cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st32407', OBJECT_OWNER, 0, 0)
        cl_evact.StateCBUsePerform(oTarget, oEventCB, 8607, 0, {
            'Att': (lambda *a: (Func597(*a) * 40 + 1600 + 600 * Func223(*a)) * 100),
            'Cnt': (lambda *a: 3 + Func597(*a) // 40) }, 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB):
        cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st32407', OBJECT_OWNER, 0, 0)


class CState(cl_state.CState):
    m_SID = 32407
    m_Name = '#NT#迅影流星技能释放2级'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

