# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1684.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1684.pyc
# Source Generated with Decompyle++
# File: st1684.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_HERO
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, -1, None)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, 25815)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_HERO, None, 0, 0, 0, 0, { }, -1, None, None, None, None)
    if cl_evcon.GetThisTargetNum(oTarget, oEventCB) >= 1:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -1, None)
    else:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, 1, None)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) >= 20:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 5000, 0, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 200), 0, 0, '')


def CallBack3(oEventCB, oTarget):
    if cl_evcon.StateCBGetSelfCount(oTarget, oEventCB) > 0:
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
        cl_action.StateAddState(oTarget, oEventCB.GetCBLifeCycle(), 1822, 50, { }, None)


class CState(cl_state.CState):
    m_SID = 1684
    m_Name = '#NT#孤狼只影（怪物遗物）'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3 }

