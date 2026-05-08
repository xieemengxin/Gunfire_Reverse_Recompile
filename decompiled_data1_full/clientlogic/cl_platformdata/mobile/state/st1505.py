# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1505.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1505.pyc
# Source Generated with Decompyle++
# File: st1505.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_object
import cl_snetwar
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def DelayAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'State': 1204 })


class CState(cl_state.CState):
    m_SID = 1505
    m_Name = '起死回生'
    m_DieRemove = 1
    m_IsShow = 1
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
        'delay': 1000,
        'firsttime': 996,
        'cnt': 1 }


def CustomAction(oWarrior, oLifeCycle, dInfo):
    if oWarrior.m_State.GetItemBySID(dInfo['State']):
        return None
    oReason = cl_object.reason.CStrReason('st1505')
    oDieElement = oWarrior.m_Game.m_WarMgr.GetComponent('PVEDieElement')
    if not oDieElement:
        return None
    oDieElement.HeroEnterDie(oWarrior, 0, oReason)

