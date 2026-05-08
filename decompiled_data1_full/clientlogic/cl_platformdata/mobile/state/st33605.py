# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33605.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33605.pyc
# Source Generated with Decompyle++
# File: st33605.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ALL, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func589

def StateRemoveAction(oTarget, oLifeCycle):
    if not cl_condition.StateCheckStatistics(oTarget, oLifeCycle, 'KeepBigLion'):
        cl_action.CommonChangeEnergy(oTarget, oLifeCycle, (lambda *a: -Func304(*a, **{
'sAttr': 'Energy' })), 0)
        cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: Func589(*a)), 0, DAM_USE_ALL)
        cl_action.CommonRemoveOwnerState(oTarget, oLifeCycle, 33604, 0)


class CState(cl_state.CState):
    m_SID = 33605
    m_Name = '怒罡化形'
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
    m_Action = (None, StateRemoveAction)

