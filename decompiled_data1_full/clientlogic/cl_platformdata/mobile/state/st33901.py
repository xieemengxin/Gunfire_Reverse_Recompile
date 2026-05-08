# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33901.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33901.pyc
# Source Generated with Decompyle++
# File: st33901.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckNowCountEqualMaxCount(oTarget, oLifeCycle) or cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 0:
        cl_action.CommonClearChangeThrowPerformUse(oTarget, oLifeCycle)
        cl_action.StateSetArgValue(oTarget, oLifeCycle, 'NoCostBullet', 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NoCostBullet'):
        cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'NoCostBullet', 1)
        cl_action.CommonChangeThrowPerformUse(oTarget, oEventCB.GetCBLifeCycle(), 0, 1426)


class CState(cl_state.CState):
    m_SID = 33901
    m_Name = '极致改装温度'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 100
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

