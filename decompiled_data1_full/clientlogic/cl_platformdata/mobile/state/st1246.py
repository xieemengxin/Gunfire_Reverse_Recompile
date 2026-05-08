# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1246.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1246.pyc
# Source Generated with Decompyle++
# File: st1246.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_ABNORMAL, STATE_EFF_DEBAR

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonSetImmobilize(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })


class CState(cl_state.CState):
    m_SID = 1246
    m_Name = '#NT#玩家复活锁定怪物'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_DEBAR
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
    m_Action = (StateActAction, StateRemoveAction)


def CustomAction(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
    if not oAttack:
        return None
    iLastFrame = oGame.GetFrameNum() - oState.m_CreateFrame

