# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33830.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33830.pyc
# Source Generated with Decompyle++
# File: st33830.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'MoveSpeed', (lambda *a: -Func404(*a)), 0, 0)


class CState(cl_state.CState):
    m_SID = 33830
    m_Name = '弹射飞镖敌方减速'
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10000
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }

