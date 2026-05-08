# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33699.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33699.pyc
# Source Generated with Decompyle++
# File: st33699.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEFEND_TREND_SHIELD, OBJ_SELF, STATE_ADD_REFRESHORSYNC_SAMEITEM, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func514

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oTarget, oLifeCycle, DEFEND_TREND_SHIELD):
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ShieldMax', oLifeCycle.m_Owner.GetArgValue('DefenseValueMax'), 0, 0)
    else:
        cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'ArmorMax', oLifeCycle.m_Owner.GetArgValue('DefenseValueMax'), 0, 0)
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func514(*a, **{
'sAttr': 'DefenseValueMax' }) / 100))


class CState(cl_state.CState):
    m_SID = 33699
    m_Name = '重装防御'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC_SAMEITEM
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

