# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33881.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33881.pyc
# Source Generated with Decompyle++
# File: st33881.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_TYPE_CORRISION, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, oLifeCycle.m_Owner.GetArgValue('MaxTotalDamCount'))


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, (lambda *a: Func404(*a) * 100), 0, DAM_TYPE_CORRISION, 1)


class CState(cl_state.CState):
    m_SID = 33881
    m_Name = '腐蚀凋零'
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

