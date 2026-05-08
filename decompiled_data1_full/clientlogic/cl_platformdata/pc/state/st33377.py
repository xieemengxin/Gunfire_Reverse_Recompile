# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33377.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33377.pyc
# Source Generated with Decompyle++
# File: st33377.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_ELEMENT, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 20, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'suit15104', (lambda *a: Func404(*a)))


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func404(*a) * 1))
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 60:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, 2500, DAM_MASK_ELEMENT, '')
        if not cl_evcon.CheckHitWeakness(oTarget, oEventCB, -1):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -10, None)
        elif not cl_evcon.CheckHitWeakness(oTarget, oEventCB, -1):
            cl_evact.StateAddSelfCount(oTarget, oEventCB, -10, None)


class CState(cl_state.CState):
    m_SID = 33377
    m_Name = '#NT#仁者无敌套装满层状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

