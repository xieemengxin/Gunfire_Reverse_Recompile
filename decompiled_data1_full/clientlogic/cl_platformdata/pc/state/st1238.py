# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1238.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1238.pyc
# Source Generated with Decompyle++
# File: st1238.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 0, None, None, { }, None, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 20:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, 25)
    else:
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func404(*a)))


class CState(cl_state.CState):
    m_SID = 1238
    m_Name = '孤狼只影'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 20
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
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

