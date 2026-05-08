# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32505.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32505.pyc
# Source Generated with Decompyle++
# File: st32505.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.GetStateStatistics(oTarget, oLifeCycle, 32505, 'NotSend') == 0:
        cl_action.CommonSendStateCountChangeMessage(oTarget, oLifeCycle)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1312, 'Radius', 0, (lambda *a: Func404(*a)))


class CState(cl_state.CState):
    m_SID = 32505
    m_Name = '#NT#改版桃剑心实际层数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_CountFunc = {
        'action': StateCountAction }

