# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33143.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33143.pyc
# Source Generated with Decompyle++
# File: st33143.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func402

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'ReduceDeviceCost', (lambda *a: Func402(*a) * 10))
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 50363, 'EnergyCost', (lambda *a: -Func402(*a) * 1000), 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 50364, 'EnergyCost', (lambda *a: -Func402(*a) * 1000), 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSetCustomData(oTarget, oLifeCycle, 'ReduceDeviceCost', 0)


class CState(cl_state.CState):
    m_SID = 33143
    m_Name = '#NT#屏障专属7减少耗能'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 3
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)

