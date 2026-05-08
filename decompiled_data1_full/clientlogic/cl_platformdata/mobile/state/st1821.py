# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1821.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1821.pyc
# Source Generated with Decompyle++
# File: st1821.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'TempMaxCash', 9876)
    cl_action.CommonAddWarCash(oTarget, oLifeCycle, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    oTarget.Delete('TempMaxCash')


class CState(cl_state.CState):
    m_SID = 1821
    m_Name = '#NT#幸运轮盘金币上限'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 1
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)

