# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/roundelement.pyc
# RelativePath: clientlogic/cl_warmgr/roundelement.pyc
# Source Generated with Decompyle++
# File: roundelement.pyc (Python 3.6)

from cl_only import ChooseKey, SendAlert, DeepCopy
from cl_warmgr.mobject import CBaseElement
from cl_commondefines import STATE_TIME_FOREVER, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, LEVEL_TYPE_HALL
from cl_warmgr.round import NewRoundExtRule
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_state
import cl_object.reason
import cl_notify
import cl_snetwar
import cl_formula

class CRoundElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CRoundElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        iRound = self.m_WarMgr.m_Round
        iCycle = self.m_WarMgr.m_Cycle
        self.m_DebuffList = oData.m_Debuff
        self.m_CurState = { }
        self.m_DebuffProp = oData.m_DebuffProp[iRound] if iRound in oData.m_DebuffProp else 0
        self.m_MonsterAdjust = oData.m_MonsterAttrAdjust[iRound] if iRound in oData.m_MonsterAttrAdjust else { }
        dCycleMonsterAttrAdjustInfo = oData.m_CycleMonsterAttrAdjust[iRound] if iRound in oData.m_CycleMonsterAttrAdjust else { }
        dLevelCycleMonsterAdjust = dCycleMonsterAttrAdjustInfo[iCycle] if iCycle in dCycleMonsterAttrAdjustInfo else { }
        self.m_AllCycleMonsterAdjust = [ (key, dLevelCycleMonsterAdjust[key]) for key in sorted(dLevelCycleMonsterAdjust) ]
        self.m_CycleMonsterAdjust = dLevelCycleMonsterAdjust.get((0, 0), { })
        dCycleMonsterRewardAdjustInfo = oData.m_CycleMonsterRewardAdjust[iRound] if iRound in oData.m_CycleMonsterRewardAdjust else { }
        self.m_CycleMonsterRewardAdjust = dCycleMonsterRewardAdjustInfo[iCycle] if iCycle in dCycleMonsterRewardAdjustInfo else { }
        self.m_ModeMonsterAttrAdjust = self.GetModeMonsterAttrAdjust()
        lstExtRuleKey = [
            (iRound, iCycle),
            (0, 0)]
        self.m_ExtRuleParam = { }
        for tExtRuleKey in lstExtRuleKey:
            if tExtRuleKey not in oData.m_ExtRule:
                continue
            self.m_ExtRuleParam.update(oData.m_ExtRule[tExtRuleKey])
        
        self.m_ExtRule = { }
        self.m_FirstCycleHero = { }
        if (0) < oGame.m_WarMgr.m_Cycle:
            pass
        elif oGame.m_WarMgr.m_Cycle < 9:
            pass
        
        self.m_CycleGSCashRelief = 100
        dMonsterRecvDamAdjust = oData.m_Config.get('MonsterRecvDamAdjust', { })
        self.m_MonsterRecvDamAdjust = dMonsterRecvDamAdjust.get((iRound, iCycle), { })
        self.m_BendShopInfo = {
            'SleepBendShopNpc': oData.m_Config.get('SleepBendShopNpc', 0),
            'SleepBendShopLayer': oData.m_Config.get('SleepBendShopLayer', 0),
            'BendShopNpc': oData.m_Config.get('BendShopNpc', 0) }

    
    def InitAfter(self):
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl and self.m_DebuffProp:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, 'RoundRoomStart')
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, 'RoundRoomGoal')
            oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerReEnter, 'RoundRoomReEnter')
        if oWarMgr.m_Cycle > 0:
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, 'RoundStartFight')
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnAddPlayer, 'RoundAddPlayer', iOnce = 0)
        for iType, dParam in self.m_ExtRuleParam.items():
            self.AddRoundExtRule(iType, dParam, 'RoundInitAfter')
        
        if len(self.m_AllCycleMonsterAdjust) > 1:
            oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, 'RoundLevelNodeInit')

    
    def AddRoundExtRule(self, iType, dParam, sReason):
        if iType in self.m_ExtRule:
            SendAlert('err', '周目额外规则重复 %s %s %s' % (iType, self.m_ExtRule, sReason))
            return None
        self.m_ExtRule[iType] = NewRoundExtRule(self, self.m_Game, iType, dParam)

    
    def OnRoomStart(self, oRoundElement, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType != LEVEL_TYPE_FIGHT:
            return None
        oGame = self.m_Game
        if oGame.Random(100) < self.m_DebuffProp:
            iState = ChooseKey(oGame, self.m_DebuffList)
            if not iState:
                return None
            iRoom = dMsgInfo['Room']
            tKey = (iLevel, iRoom)
            self.m_CurState[tKey] = iState
            self.RefreshNotify(self.m_WarMgr.GetLivePlayer())
            oReason = cl_object.reason.CStrReason('RoundDebuff')
            for iHero in self.m_WarMgr.GetLiveHero():
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                oState = cl_state.AddState(oHero, iState, STATE_TIME_FOREVER, 0, {
                    'AID': 0,
                    'RS': oReason })
                if not oState:
                    continue
                oState.Enable(oHero)
            

    
    def OnRoomGoal(self, oRoundElement, oLevelCtrl, dMsgInfo):
        iRoom = dMsgInfo['Room']
        iLevel = dMsgInfo['Level']
        tKey = (iLevel, iRoom)
        if tKey not in self.m_CurState:
            return None
        iState = self.m_CurState.pop(tKey)
        self.RefreshNotify(self.m_WarMgr.GetLivePlayer())
        oGame = self.m_Game
        for iHero in self.m_WarMgr.GetLiveHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            cl_state.RemoveState(oHero, iState)
        

    
    def OnPlayerReEnter(self, oWarMgr, oHero, dInfo):
        self.RefreshNotify([
            oHero.m_PlayerID])

    
    def OnAddPlayer(self, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['Hero']
        dPlayerInfo = dMsgInfo['Info']
        if 'FirstCycle' not in dPlayerInfo or not dPlayerInfo['FirstCycle']:
            iCycleGSCashRelief = cl_formula.GetFormulaResult(oHero, self.m_CycleGSCashRelief, { })
            oHero.SetSavedData('CycleGSCashRelief', iCycleGSCashRelief)
            return None
        oHero.SetSavedData('CycleGSCashRelief', 0)
        WarobjLog.Info('firstcycle %s-%s' % (self.m_Game.m_ID, oHero.m_PlayerID))
        iHeroID = oHero.m_ID
        self.m_FirstCycleHero[iHeroID] = 1
        cl_msgcenter.AddAttentionFunc(self, iHeroID, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerLoadOK, 'RefreshFirstCycle')
        if len(self.m_FirstCycleHero) == 1:
            cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, 'FirstCycleDoneAttention')

    
    def OnPlayerLoadOK(self, oRoundElement, oHero, dMsgInfo):
        cl_snetwar.GS2CIsFirstCycle(oHero.m_PlayerID, iIsFirstCycle = 1)

    
    def OnLevelNodeFinish(self, oWarMgr, dMsgInfo):
        for iHeroID in self.m_FirstCycleHero:
            cl_msgcenter.DoneAttention(self, iHeroID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'RefreshFirstCycle')
        
        self.m_FirstCycleHero.clear()

    
    def OnLevelNodeInit(self, oWarMgr, oHero, dInfo):
        if dInfo['LevelType'] not in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            return None
        iCurLayer = dInfo['Layer']
        iCurLevel = dInfo['Level']
        for (iLayer, iLevel), dAdjust in self.m_AllCycleMonsterAdjust:
            if iLayer > iCurLayer:
                break
            if iLayer == iCurLayer and iLevel > iCurLevel:
                break
            self.m_CycleMonsterAdjust = dAdjust
        

    
    def OnStartFight(self, oRoundElement, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType != LEVEL_TYPE_HALL:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oWarMgr.GetComponent('SnowMountainElement') and oLevelCtrl.m_LayerNum == self.m_BendShopInfo['SleepBendShopLayer']:
            iNpcID = self.m_BendShopInfo['SleepBendShopNpc']
        else:
            iNpcID = self.m_BendShopInfo['BendShopNpc']
        iLevelID = dMsgInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
        dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'bendshoppos')
        if not dAddInfo:
            return None
        dAddInfo = DeepCopy(dAddInfo)
        iScene = oLevelNode.m_Scene
        dMsgInfo = {
            'NPC': iNpcID,
            'LevelNode': oLevelNode,
            'NPCInfo': dAddInfo,
            'Scene': iScene }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
        if not dMsgInfo['NPC']:
            return None
        self.m_Game.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)

    
    def RefreshNotify(self, lstPlayer):
        lstText = []
        for iState in self.m_CurState.values():
            clsState = cl_state.GetStateClass(iState)
            if clsState:
                lstText.append(clsState.m_Desc)
        
        if not lstText:
            cl_notify.ClearCommonNotify(self.m_Game, lstPlayer, 2116)
            return None
        sText = '\n'.join(lstText)
        cl_notify.SendCommonNotify(self.m_Game, lstPlayer, 2116, {
            '$text': sText })

    
    def Release(self):
        oGame = self.m_Game
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl and self.m_DebuffProp:
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, 'RoundRoomStart')
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, 'RoundRoomGoal')
            oGame.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'RoundRoomReEnter')
        for iHero, sKey in self.m_FirstCycleHero.items():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, sKey)
        
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'RoundStartFight')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, 'RoundAddPlayer')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'FirstCycleDoneAttention')
        if len(self.m_AllCycleMonsterAdjust) > 1:
            oGame.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'RoundLevelNodeInit')
        self.m_WarMgr = None
        for oExtRule in self.m_ExtRule.values():
            oExtRule.Release()
        
        super(CRoundElement, self).Release()

    
    def GetModeMonsterAttrAdjust(self):
        iRound = self.m_WarMgr.m_Round
        dTotalAttrAdjust = { }
        dModeMonsterAttrAdjust = self.m_Data.m_ModeMonsterAttrAdjust[iRound] if iRound in self.m_Data.m_ModeMonsterAttrAdjust else { }
        for iMode, dAttrAdjust in dModeMonsterAttrAdjust.items():
            if iMode not in self.m_WarMgr.m_ModeType:
                continue
            for sAttr, iValue in dAttrAdjust.items():
                if sAttr not in dTotalAttrAdjust:
                    dTotalAttrAdjust[sAttr] = iValue
                    continue
                dTotalAttrAdjust[sAttr] += iValue
            
        
        return dTotalAttrAdjust



def GetComponentClass(oMgrManager):
    return CRoundElement

