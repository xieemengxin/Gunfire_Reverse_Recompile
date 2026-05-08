# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4042.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4042.pyc
# Source Generated with Decompyle++
# File: p4042.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object
import cl_state
import cl_snetwar
from cl_only import Functor, PY_FLAG_DEAD
from cl_commondefines import MODEL_TYPE_POINT, DAM_TYPE_TRUE, DAM_USE_HP, STATE_TIME_LIMIT, STATE_TIME_FOREVER
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_USE_HP, FIGHT_KEY_WUDI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 1042)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'Att', 1500, 0, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 0, -2000000, None)
    cl_action.CommonChangeDefValue(oWarrior, oLifeCycle, 6000000, DAM_USE_HP)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'TurnSpeed', 0, 200, None)
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, None)
    oLifeCycle.m_Owner.CustomAction(oWarrior, oLifeCycle, {
        'Summon': {
            1011: 1,
            1010: 1 },
        'State': 7023,
        'Time': 200 })
    cl_action.HaltAllCasting(oWarrior, oLifeCycle.Key())
    cl_action.CommonSummonObstacleUsePerform(oWarrior, oLifeCycle, 1, 1606)
    cl_action.CommonSummonObstacleUsePerform(oWarrior, oLifeCycle, 2, 1606)
    cl_action.CommonSummonObstacleUsePerform(oWarrior, oLifeCycle, 3, 1606)
    cl_action.CommonSummonObstacleUsePerform(oWarrior, oLifeCycle, 4, 1606)
    cl_action.CommonSummonObstacleUsePerform(oWarrior, oLifeCycle, 5, 1606)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7025, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7028, 1, None, None)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 7031, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 4042
    m_Name = '组队BOSS-阶段4'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    
    def CustomAction(self, oWarrior, oLifeCycle, dInfo):
        
        def ClearCustomAction(oTarget, pfobj):
            sKey = pfobj.Key()
            oGame = oTarget.m_Game
            lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
            cl_snetwar.GS2CDoubleHPBarUI(oGame, [], 0, lstPlayer)
            oGame.DoneGlobalAttention(oTarget.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, sKey)
            lstSummon = oTarget.Query('BodyPart', [])
            for iSummon in lstSummon:
                oSummon = oGame.GetObject(iSummon)
                if not oSummon:
                    continue
                oSummon.Remove(sKey)
            

        pfobj = oLifeCycle.GetObject()
        iScene = oWarrior.m_Scene
        oGame = oWarrior.m_Game
        dSummonSID = dInfo['Summon'] if 'Summon' in dInfo else { }
        iState = dInfo['State'] if 'State' in dInfo else 0
        iTime = dInfo['Time'] if 'Time' in dInfo else -1
        iTimeType = STATE_TIME_LIMIT if iTime else STATE_TIME_FOREVER
        oReason = cl_object.reason.CPerformReason(pfobj.m_SID, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType)
        dAddInfo = {
            'Shape': MODEL_TYPE_POINT,
            'Side': oWarrior.m_Side,
            'Grade': oWarrior.m_Grade,
            'Origin': oWarrior.GetPos(),
            'Owner': oWarrior.m_ID }
        lstSummon = []
        for iSummonSID in dSummonSID:
            oSummon = oGame.m_ResMgr.CreateSummon(iScene, iSummonSID, dAddInfo)
            if not oSummon:
                continue
            iSummon = oSummon.m_ID
            lstSummon.append(iSummon)
            if not iState or iTime == -1:
                continue
            dArgs = {
                'AID': oWarrior.m_ID,
                'RS': oReason,
                'pfid': pfobj.m_SID,
                'PFLV': pfobj.m_Level,
                'arg': { } }
            oState = cl_state.AddState(oSummon, iState, iTimeType, iTime, dArgs)
            if not oState:
                continue
            oState.Enable(oSummon)
        
        if not lstSummon:
            WarriorDie(oWarrior, pfobj.m_SID)
            return None
        iMsg = cl_msgcenter.MSG_WAR_DIE
        sKey = pfobj.Key()
        for iSummon in lstSummon:
            cl_msgcenter.AddAttentionFunc(oWarrior, iSummon, iMsg, Functor(OnBodyPartDie, pfobj.m_SID, iMsg, sKey), sKey)
        
        oWarrior.Set('BodyPart', lstSummon)
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
        cl_snetwar.GS2CDoubleHPBarUI(oGame, lstSummon, 1, lstPlayer)
        oGame.AddGlobalAttention(oWarrior.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, OpenDoubleHPBarUI, sKey)
        oLifeCycle.AddDisableFunc(ClearCustomAction)



def OpenDoubleHPBarUI(oListener, oSender, dInfo):
    oGame = oListener.m_Game
    lstPlayer = [
        oSender.m_PlayerID]
    lstSummon = oListener.Query('BodyPart', [])
    cl_snetwar.GS2CDoubleHPBarUI(oGame, lstSummon, 1, lstPlayer)


def OnBodyPartDie(iPerform, iMsg, sKey, oWarrior, oSender, dInfo):
    cl_msgcenter.DoneAttention(oWarrior, oSender.m_ID, iMsg, sKey)
    lstSummon = oWarrior.Query('BodyPart', [])
    for iSummon in lstSummon:
        oSummon = oWarrior.m_Game.GetObject(iSummon, PY_FLAG_DEAD)
        if oSummon:
            break
    


def WarriorDie(oWarrior, iPerform):
    oReason = cl_object.reason.CPerformReason(iPerform, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType).ExtInfo({
        'ShowTips': 0,
        'DamType': DAM_TYPE_TRUE | DAM_USE_HP })
    lstChange = [
        (oWarrior.HP(), oReason)]
    oWarrior.HPModifyDam(oWarrior.m_ID, lstChange)

