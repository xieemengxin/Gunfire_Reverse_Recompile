# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33793.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33793.pyc
# Source Generated with Decompyle++
# File: st33793.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, PERFORMCDRATE_TYPE_PASSIVE, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonAddPerformCDTimer(oTarget, oLifeCycle, 12, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle):
        cl_action.CommonChangePerformCDRate(oTarget, oLifeCycle, PERFORMCDRATE_TYPE_PASSIVE, (lambda *a: Func404(*a)), 0)
    else:
        oTarget.m_State.RemoveItem(oLifeCycle.m_Owner.m_ID)


class CState(cl_state.CState):
    m_SID = 33793
    m_Name = '骰子冷却速度加快'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 65535
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

