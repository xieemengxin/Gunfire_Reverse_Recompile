# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33442.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33442.pyc
# Source Generated with Decompyle++
# File: st33442.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    if cl_action.CommonGetSeasonSuitArg(oTarget, oLifeCycle, 15110, '15110Save', 1):
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, cl_action.CommonGetSeasonSuitArg(oTarget, oLifeCycle, 15110, '15110Count', 1))
    else:
        cl_action.CommonSetSeasonSuitArg(oTarget, oLifeCycle, 15110, '15110Save', 1, 1)
        cl_action.StateSetSelfCount(oTarget, oLifeCycle, 4)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetSeasonSuitArg(oTarget, oLifeCycle, 15110, '15110Count', (lambda *a: Func404(*a)), 1)


class CState(cl_state.CState):
    m_SID = 33442
    m_Name = '#NT#顺其自然计数'
    m_IsShow = 1
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }

