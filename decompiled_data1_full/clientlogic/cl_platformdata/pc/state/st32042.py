# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32042.pyc
# Source Generated with Decompyle++
# File: st32042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func410

def DelayAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func410(*a, **{
'sid': 32035 }))) <= 0:
        cl_action.CommonAddStateCount(oTarget, oLifeCycle, 32035, 1, None)


class CState(cl_state.CState):
    m_SID = 32042
    m_Name = '#NT#绝处逢生lv.3'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_DelayAction = {
        'action': DelayAction,
        'delay': 400,
        'firsttime': 400 }

