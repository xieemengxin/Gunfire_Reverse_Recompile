# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33552.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33552.pyc
# Source Generated with Decompyle++
# File: st33552.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func361, Func404

def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetPerformArgs(oTarget, oLifeCycle, 1970, 'AngleSpeed', (lambda *a: max(-360, int(Func361(*a, **{
'sid': 1970,
'sArgs': 'BaseSpeed' }) - 60 * Func404(*a)))), None)


class CState(cl_state.CState):
    m_SID = 33552
    m_Name = '星轨加速'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 60000
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

