# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8101.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8101.pyc
# Source Generated with Decompyle++
# File: st8101.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, DAM_USE_SHIELD, OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) > 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckStateAddByIs(oTarget, oEventCB, None):
        cl_evact.StateAddSelfCountByFinalDamage(oTarget, oEventCB, 10, -1)


def CallBack1(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 1, None)
    cl_evact.EventCBGetTargetByBelongs(oTarget, oEventCB)
    cl_evact.EventTargetDamage(oTarget, oEventCB, cl_action.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()), DAM_TYPE_PERSISTENCE | DAM_TYPE_TRUE | DAM_USE_ALL, -1, 0, 0, 0, 0, 0, 0, 0, None, None, None)
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 0)


class CState(cl_state.CState):
    m_SID = 8101
    m_Name = '#NT#妖王-分身溅射'
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 999999999
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
        'delay': 4,
        'firsttime': 4 }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

