# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32905.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32905.pyc
# Source Generated with Decompyle++
# File: st32905.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 1:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, -1, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 32920, '13537') > 0:
        cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oTarget, oEventCB, 32775, 10, 200, -1)
        cl_evact.EventCBAddStateStatistics(oTarget, oEventCB, -1, 32920, '13537')
    cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)


class CState(cl_state.CState):
    m_SID = 32905
    m_Name = '#NT#左右互博特种弹'
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

