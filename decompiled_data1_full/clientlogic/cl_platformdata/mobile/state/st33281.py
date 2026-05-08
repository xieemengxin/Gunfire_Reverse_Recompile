# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33281.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33281.pyc
# Source Generated with Decompyle++
# File: st33281.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateCheckSourceWeaponHasInscription(oTarget, oLifeCycle, 13087):
        cl_action.StateChangeSourceWeaponAttr(oTarget, oLifeCycle, 'Att', 0, 1000 * cl_action.StateGetSelfCount(oTarget, oLifeCycle))


class CState(cl_state.CState):
    m_SID = 33281
    m_Name = '#NT#13087能量基伤增益'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        'delay': 100,
        'firsttime': 100 }
    m_CountFunc = {
        'action': StateCountAction }

