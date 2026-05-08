# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33043.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33043.pyc
# Source Generated with Decompyle++
# File: st33043.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_ARMOR, DEFEND_TREND_SHIELD, OBJ_FRIEND, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func514

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ArmorMax', 0, (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000), 0)
    elif cl_condition.CheckTargetDefendTrend(oTarget, oEventCB.GetCBLifeCycle(), DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oEventCB.GetCBLifeCycle(), 'ShieldMax', 0, (lambda *a: Func514(*a, **{
'sAttr': 'TalentLevel' }) * 5000), 0)


class CState(cl_state.CState):
    m_SID = 33043
    m_Name = '#NT#处决大师Q6天赋-临时护盾上限状态'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_FRIEND
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
    m_CBFuncAction = {
        1: CallBack1 }

