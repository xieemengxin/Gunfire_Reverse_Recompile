# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33433.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33433.pyc
# Source Generated with Decompyle++
# File: st33433.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func404

def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', 0, (lambda *a: 1500 * Func404(*a)), 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', 0, (lambda *a: 1500 * Func404(*a)), 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetRangeTargetByFightType(oTarget, oEventCB, 12, WARRIOR_MONSTER, 1, 0, 0, 0, 0, { }, 0, None, None, None, None)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, cl_evact.EventCBCalCountByMonsterFightType(oTarget, oEventCB, {
        'Normal': 1,
        'Elite': 3,
        'Boss': 10 }))


class CState(cl_state.CState):
    m_SID = 33433
    m_Name = '游刃有余'
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

