# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1179.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1179.pyc
# Source Generated with Decompyle++
# File: st1179.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_only import Functor
from cl_commondefines import INSCRIPTION_SPORE
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE

class CState(cl_state.CState):
    m_SID = 1179
    m_Name = '#NT#铭刻4841'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 99
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1


def CustomAction(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iAttack = oState.m_Attacker
    sKey = oState.Key()
    cl_msgcenter.AddAttentionFunc(oTarget, iAttack, cl_msgcenter.MSG_WAR_DISABLE_GEMINI, Functor(OnDisable, oState.m_ID, sKey), sKey)


def OnDisable(iStateID, sKey, oTarget, oAttack, dInfo):
    cl_msgcenter.DoneAttention(oTarget, oAttack.m_ID, cl_msgcenter.MSG_WAR_DISABLE_GEMINI, sKey)
    if dInfo['SID'] == INSCRIPTION_SPORE:
        oTarget.m_State.RemoveItem(iStateID)

