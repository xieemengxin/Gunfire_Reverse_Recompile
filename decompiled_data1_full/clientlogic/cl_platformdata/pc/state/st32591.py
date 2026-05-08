# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32591.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32591.pyc
# Source Generated with Decompyle++
# File: st32591.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_math
from cl_only import Functor
from cl_commondefines import WARRIOR_MONSTER, WARRIOR_SUMMON
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, {
        'SummonID': (1024, 1053, 1028),
        'StateSID': 32585,
        'Range': 10,
        'MaxCount': 5,
        'StateTime': (800, 800, 1000) })


class CState(cl_state.CState):
    m_SID = 32591
    m_Name = '#NT#海纳百川监听怪物死亡'
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
    m_Action = (StateActAction, None)


def CustomAction(oWarrior, oLifeCycle, dInfo):
    
    def ClearEvent(oOwner, oLifeCycle):
        oOwner.m_Game.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, sKey, -1)

    iTarget = oWarrior.m_ID
    sKey = oLifeCycle.Key()
    oWarrior.m_Game.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, Functor(OnDie, dInfo, oLifeCycle), sKey, -1)
    oLifeCycle.AddDisableFunc(ClearEvent)


def OnDie(dInfo, oLifeCycle, oListener, oVictim, dMsgInfo):
    if (oVictim.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER or oVictim.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON) and oVictim.m_DataSID in dInfo['SummonID'] and cl_math.CheckDistance3D(oListener.GetPos(), oVictim.GetPos(), dInfo['Range']):
        oTalent = oListener.m_TalentCon.GetPerform(2917)
        if not oTalent:
            return None
        iLevel = oTalent.m_Level
        iTime = dInfo['StateTime'][iLevel - 1]
        cl_action.StateAddState(oListener, oLifeCycle, dInfo['StateSID'], iTime, { })
        oState = oListener.m_State.GetItemBySID(dInfo['StateSID'])
        if not oState:
            return None
        iCount = oState.GetCount()
        if iCount < dInfo['MaxCount']:
            oState.AddCount(oListener, 1)

