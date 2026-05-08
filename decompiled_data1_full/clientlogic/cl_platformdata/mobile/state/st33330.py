# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33330.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33330.pyc
# Source Generated with Decompyle++
# File: st33330.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJECT_SELFOWNER, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func3, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if not cl_condition.StateCheckStatistics(oTarget, oLifeCycle, 'IsStop'):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 20:
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33330, (lambda *a: Func404(*a) // 20), 'SpellNum')
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func3(*a, **{
'a': int(Func404(*a)),
'b': 20 })))
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBUseEnableSpell(oTarget, oEventCB, cl_evact.EventCBGetStateStatistics(oTarget, oEventCB, 33330, 'SpellNum'), 1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventCBRecordMoveDis(oTarget, oEventCB, 'st33330', OBJECT_SELFOWNER, 1)
    cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), cl_evact.EventCBGetMoveDis(oTarget, oEventCB, 'st33330', OBJECT_SELFOWNER, 1), None)
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st33330', OBJECT_SELFOWNER, 0, 1)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 1, 33330, 'IsStop')


def CallBack3(oEventCB, oTarget):
    cl_evact.EventCBResetMoveDis(oTarget, oEventCB, 'st33330', OBJECT_SELFOWNER, 0, 1)
    cl_evact.EventCBSetStateStatistics(oTarget, oEventCB, 0, 33330, 'IsStop')


class CState(cl_state.CState):
    m_SID = 33330
    m_Name = '#NT#移动妖灵攻击'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50,
        'firsttime': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3 }

