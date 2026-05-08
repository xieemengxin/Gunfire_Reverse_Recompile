# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32875.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32875.pyc
# Source Generated with Decompyle++
# File: st32875.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_USE_ALL, OBJ_SELF, STATE_ADD_REFRESHORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403, Func404

def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateCureByAtive(oTarget, oLifeCycle, (lambda *a: (Func403(*a, **{
'sAttr': 'HPMax' }) + Func403(*a, **{
'sAttr': 'ShieldMax' }) + Func403(*a, **{
'sAttr': 'ArmorMax' })) * Func404(*a) / 100), 1, DAM_USE_ALL)


class CState(cl_state.CState):
    m_SID = 32875
    m_Name = '#NT#赌侠有借必还'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
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

