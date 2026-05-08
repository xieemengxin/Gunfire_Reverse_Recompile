# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st1005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st1005.pyc
# Source Generated with Decompyle++
# File: st1005.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_snetwar
from cl_commondefines import WARRIOR_SERVANT, WARRIOR_HERO
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonForceSetAttr(oTarget, oLifeCycle, 'MoveSpeed', 100)


class CState(cl_state.CState):
    m_SID = 1005
    m_Name = '#NT#濒死状态'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 100
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_GameBroadcast = 1
    m_Action = (StateActAction, None)
    
    def OnCountFull(self, oTarget, dInfo):
        oTarget.m_State.RemoveItem(self.m_ID)
        oDieElement = oTarget.m_Game.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement:
            if oTarget.m_FightType & WARRIOR_SERVANT:
                oDieElement.RealServantDie(oTarget)
            elif oTarget.m_FightType & WARRIOR_HERO:
                if oTarget.m_Game.m_WarMgr.IsSingleGame():
                    cl_snetwar.GS2CRelifeConfirm(oTarget.m_Game, oTarget.m_PlayerID, iRelifeIdx = 0, iLeftTimes = 0, iMaxTimes = 0, iType = 0, iRemainTime = 0, iCost = 0)
                oDieElement.RealHeroDie(oTarget)


