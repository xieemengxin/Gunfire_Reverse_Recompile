# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8072.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8072.pyc
# Source Generated with Decompyle++
# File: st8072.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, PLAYMODE_NEWSURVIVOR, PLAYMODE_SURVIVOR, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    if cl_condition.CheckWarPlayMode(oTarget, oLifeCycle, PLAYMODE_SURVIVOR) or cl_condition.CheckWarPlayMode(oTarget, oLifeCycle, PLAYMODE_NEWSURVIVOR):
        cl_action.CommonSuperMonster(oTarget, oLifeCycle, {
            6165: 10 }, {
            6251: 10,
            6252: 10,
            6253: 10,
            6254: 10 })
    else:
        cl_action.CommonSuperMonster(oTarget, oLifeCycle, {
            6115: 10 }, {
            6201: 10,
            6202: 10,
            6203: 10,
            6204: 10 })


class CState(cl_state.CState):
    m_SID = 8072
    m_Name = '#NT#传承强化'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_ENEMY
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

